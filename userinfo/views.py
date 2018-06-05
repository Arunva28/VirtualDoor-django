from .serializers import BasicUserSerializer, AddUserSerializer
from .models import BasicUserInfo, UserInfo
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


# Create your views here.
@method_decorator(csrf_exempt, name='post')
class UserRecordView(APIView):
    authentication_classes = [BasicAuthentication, CsrfExemptSessionAuthentication]
    serializer_class = AddUserSerializer

    def get(self, request, format=None):
        email = request.user.email
        user = UserInfo.objects.get(user=email)
        is_admin = user.isAdmin
        if is_admin is True:
            print("admin")
            users = UserInfo.objects.all()
            serializer = AddUserSerializer(users, many=True)
           # del (list(serializer.data)[0]["password"])
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
             print("Not an admin")
             content = {'user_id': user.user_id, 'building_name': user.buildingName, 'unit_no': user.unitNo}
             return Response(content, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AddUserSerializer(data=request.data)
        email = request.user.email
        user = UserInfo.objects.get(user=email)
        is_admin = user.isAdmin
        if is_admin is True:
            serializer = AddUserSerializer(data=request.data)
            if serializer.is_valid(raise_exception=ValueError):
                user = serializer.create(validated_data=request.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("Not authorized", status=status.HTTP_401_UNAUTHORIZED)


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        data1 = request.data
        username = data1['username']
        password = data1['password']
        valid_user = authenticate(username=username, password=password)
        if valid_user is not None:
            login(request, valid_user)
            serializer = self.serializer_class(data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            user_info = UserInfo.objects.get(user_id=user)
            content = {
                'token': token.key, 'user_id': user.pk, 'email': user.email,
                'building_name': user_info.buildingName, 'unit_no': user_info.unitNo
            }
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response("Invalid credentials", status=status.HTTP_401_UNAUTHORIZED)


@login_required
@api_view(['POST', 'GET'])
def user_logout(request):
    print("logging off")
    logout(request)
    return Response("You are logged out")


@method_decorator(csrf_exempt, name='delete')
class UserOperations(APIView):
    print("tillhere")
    authentication_classes = [BasicAuthentication, CsrfExemptSessionAuthentication]
    serializer_class = BasicUserSerializer

    def delete(self, request, email):
        admin_email = request.user.email
        user = UserInfo.objects.get(user=admin_email)
        is_admin = user.isAdmin
        if is_admin is True:
            try:
                user = BasicUserInfo.objects.get(email=email)
                user.delete()
                return Response("User Deleted Successfully", status=status.HTTP_200_OK)
            except BasicUserInfo.DoesNotExist:
                return Response("User Not found", status=status.HTTP_404_NOT_FOUND)
        else:
            return Response("Unauthorized access", status=status.HTTP_401_UNAUTHORIZED)

