from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from userinfo.models import BasicUserInfo
from datetime import datetime


class SecurityOffice(models.Model):
    Name = models.CharField(max_length=100, default="")
    Unit = models.CharField(max_length=25, default="")
    MobileNumber = PhoneField(default="")
    VisitorMailID = models.EmailField(default="")
    user = models.EmailField(default="")
    Remarks = models.CharField(max_length=256, default="")
    Datetime = models.DateTimeField(default=datetime.now, blank=True)





