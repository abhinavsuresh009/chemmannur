from django.db import models
from utils.companybranch import CompanyBranch
from django.core.validators import RegexValidator


# validating name and comcode

validate_name = RegexValidator(
    regex='^[^\s].+[a-zA-Z]+[a-zA-Z]+$',
    message='Name must contain only alphabetic characters and cannot start or end with spaces.',
    code='invalid_name'
)
validate_comcode = RegexValidator(
    regex='^[^\s].+[a-zA-Z0-9]+[a-zA-Z0-9]+$',
    message='Company code cannot contain special characters',
    code='invalid_name'
)


# models of Company and Branch

class Company(CompanyBranch):
    comcode = models.CharField(max_length=20, unique=True, verbose_name='Company code', validators=[validate_comcode])
    comname = models.CharField(max_length=50, verbose_name= 'Company name', validators=[validate_name])
    

class Branch(CompanyBranch):
    brcode = models.CharField(max_length=20, verbose_name='Branch code')
    brname = models.CharField(max_length=50, verbose_name='Branch name', validators=[validate_name])
    company = models.ForeignKey(Company,on_delete=models.CASCADE, to_field='comcode', db_column='comcode')
