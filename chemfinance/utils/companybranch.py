
from django.db import models
from django.core.validators import RegexValidator

# Validating Phone number


phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits."
    )

class CompanyBranch(models.Model):
    
    address = models.TextField(max_length=200)
    phone = models.CharField(max_length=10, validators=[phone_regex])
    email = models.EmailField()
    
    class Meta:
        abstract = True

