from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits."
    )

validate_username = RegexValidator(
    regex='[a-zA-Z]+$',
    message='Username only contain alphabets',
    code='invalid_name'
)

class User(AbstractUser):
    username = models.CharField(unique=True, max_length=50, validators=[validate_username])
    email = models.EmailField(unique=True, max_length=254)
    phone = models.CharField(max_length=10, validators=[phone_regex])
    comcode = models.CharField(max_length=20)
    brcode = models.CharField(max_length=20)
    
  
    