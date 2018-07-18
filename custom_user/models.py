from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager


class User(BaseUser):
    objects = BaseUserManager()
    allergies = models.CharField(max_length=150, blank=True, null=True)
