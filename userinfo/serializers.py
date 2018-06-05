from rest_framework import serializers, status
from .models import *
from django.contrib.auth.hashers import make_password


class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicUserInfo
        fields = ('username', 'password', 'email')

    def validate_password(self, value):
        return make_password(value)


class AddUserSerializer(serializers.ModelSerializer):

    user = BasicUserSerializer(required=True)

    class Meta:
        model = UserInfo
        fields = ('user', 'phoneNo', 'unitNo', 'buildingName', 'isAdmin')

    def create(self, validated_data):
        user_data = validated_data.pop('user')

        user_serializer = BasicUserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
        validated_data['user_id'] = user.pk
        return super(AddUserSerializer, self).create(validated_data)
