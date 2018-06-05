from .serializers import SeurityOfficeSerializer, PrimaryKeyToSecuritySerializer
from .models import SecurityOffice
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userinfo.models import UserInfo
from django.utils import timezone
from datetime import datetime
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


@method_decorator(csrf_exempt, name='post')
class SecurityOfficeView(APIView):
    authentication_classes = [BasicAuthentication, CsrfExemptSessionAuthentication]

    def get(self, request):
        email = request.user.email
        user = UserInfo.objects.get(user=email)
        is_admin = user.isAdmin
        if is_admin is True:
            securityofficeinfo = SecurityOffice.objects.all()
            var = SecurityOffice.objects.count()
            today = datetime.today()
            print(securityofficeinfo)
            if var > 1:
                securityofficeinfo = SecurityOffice.objects.order_by('Datetime').filter(
                    Q(Datetime__gte=today) | Q(Datetime=None))
                serializer = SeurityOfficeSerializer(securityofficeinfo, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("No visitors today", status=status)
        else:
            return Response("Unauthorized access", status=status.HTTP_401_UNAUTHORIZED)

    def post(self, request):
        user = ""
        try:
            user = UserInfo.objects.get(user_id=request.data['user'])
        finally:
            if user:
                print("Test1")
                serializer = PrimaryKeyToSecuritySerializer(data=request.data)
                if serializer.is_valid(raise_exception=ValueError):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                print("Test")
                return Response(status=status.HTTP_401_UNAUTHORIZED)
