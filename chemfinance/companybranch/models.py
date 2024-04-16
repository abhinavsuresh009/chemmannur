from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator


# validating name and comcode

validate_name = RegexValidator(
    regex='[a-zA-Z]+[a-zA-Z]$',
    message='Name must contain only alphabetic characters and cannot start or end with spaces.',
    code='invalid_name'
)
validate_comcode = RegexValidator(
    regex='[a-zA-Z0-9]+$',
    message='Company code cannot contain special characters',
    code='invalid_name'
)

phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits."
    )
validation_address = RegexValidator(
        regex='^[a-zA-Z0-9\s.,#-]+$',
        message="Invalid address format."
    )

class CompanyBranch(models.Model):
    
    address = models.TextField(max_length=200,validators=[validation_address])
    phone = models.CharField(max_length=10, validators=[phone_regex])
    email = models.EmailField()
    
    class Meta:
        abstract = True



# models of Company and Branch

class Company(CompanyBranch):
    comcode = models.CharField(max_length=20, unique=True, verbose_name='Company code', validators=[validate_comcode])
    comname = models.CharField(max_length=50, verbose_name= 'Company name', validators=[validate_name])
    

class Branch(CompanyBranch):
    brcode = models.CharField(max_length=20, verbose_name='Branch code', validators=[validate_comcode], unique=True)
    brname = models.CharField(max_length=50, verbose_name='Branch name', validators=[validate_name])
    company = models.ForeignKey(Company,on_delete=models.CASCADE, to_field='comcode', db_column='comcode')
