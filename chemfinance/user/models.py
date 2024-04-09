from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    phone = models.CharField(max_length=10)
    comcode = models.CharField(max_length=20)
    brcode = models.CharField(max_length=20)
    
