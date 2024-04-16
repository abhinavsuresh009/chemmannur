from django.db import models
from utils.basemodel import *

from django.core.validators import RegexValidator

# Validating Phone number


phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="This field must be 10 Numbers."
    )
validation_address = RegexValidator(
        regex='[a-zA-Z0-9\s.,#-]+$',
        message="Invalid address format."
    )
validate_name = RegexValidator(
    regex='[a-zA-Z]+$',
    message='Name must contain only alphabetic characters',
    code='invalid_name'
)
validate_number = RegexValidator(
    regex='[0-9]$',
    message='This field must contain only Nuemeric characters',
    code='invalid_name'
)

# Create your models here.
class Customer(CommonFields):
    cusid = models.CharField(max_length = 50 , verbose_name = "Customer Id", unique=True)
    fname = models.CharField(max_length = 100 , verbose_name = "First Name", validators=[validate_name])
    mname = models.CharField(max_length = 100 , verbose_name = "Middle Name", validators=[validate_name])
    lname = models.CharField(max_length = 100 , verbose_name = "Last Name", validators=[validate_name])
    address1 = models.TextField(validators=[validation_address])
    address2 = models.TextField(validators=[validation_address])
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    country = models.CharField(max_length = 100)
    pin =  models.CharField(max_length = 50, validators=[validate_number])
    dob = models.DateField(verbose_name="Date of Birth")
    gender = models.CharField(max_length = 20)
    occupation = models.CharField(max_length = 50)
    mob =  models.CharField(max_length = 20)
    phone =  models.CharField(max_length = 20, validators=[phone_regex])
    email =  models.EmailField()
    sal = models.CharField(max_length = 20 , verbose_name = "Salutation")
    aadhaar =  models.CharField(max_length = 20)
    pan =  models.CharField(max_length = 20)
    othidname =  models.CharField(max_length = 50 ,blank=True,verbose_name = "Id Collected Name")
    othid =  models.CharField(max_length = 50 ,blank=True,verbose_name = "Id Collected Number")




