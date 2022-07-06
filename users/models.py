from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
