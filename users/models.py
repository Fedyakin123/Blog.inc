from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
