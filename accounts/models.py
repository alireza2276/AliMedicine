from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.PositiveIntegerField(unique=True, null=True, blank=True)



