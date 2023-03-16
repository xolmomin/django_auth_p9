from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
