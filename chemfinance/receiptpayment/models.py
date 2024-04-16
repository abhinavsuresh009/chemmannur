from django.db import models
from utils.basemodel import CommonFields
from django.core.validators import RegexValidator

# Create your models here.
validate_name = RegexValidator(
    regex='[a-zA-Z0-9]+$',
    message='Name must contain only alphabetic characters',
    code='invalid_name'
)
class ReceiptPayment(CommonFields):
    TRANSACTION_TYPES = (
        ('Q', 'Q'),
        ('C', 'C'),
    )
       
    hcode = models.CharField( max_length=100, verbose_name='Head code')
    hcode1 = models.CharField( max_length=100, verbose_name='Sub head')
    name = models.CharField(max_length=100, validators=[validate_name])
    code = models.CharField(max_length=100)
    credit = models.FloatField(default=0)
    debit = models.FloatField(default=0)    
    vono = models.BigIntegerField(verbose_name='Voucher number')
    type = models.CharField(max_length=100, choices= TRANSACTION_TYPES)
    chkdate = models.DateTimeField(verbose_name='Check date')
    chkno = models.CharField(max_length=100, verbose_name='Check number')
    bank = models.CharField(max_length=100, validators=[validate_name])
    ifsc = models.CharField(max_length=100)
    acno = models.CharField(max_length=100, verbose_name='Account number')
    mode = models.CharField(max_length=100)
    
class BankEntry(CommonFields):
    hcode = models.CharField(max_length=100, verbose_name= 'Head code')
    hcode1 = models.CharField(max_length=100, verbose_name= 'Sub name')
    party_name = models.CharField(max_length=100, validators=[validate_name])
    code = models.CharField(max_length=100)
    credit = models.FloatField(default=0)
    debit = models.FloatField(default=0)
    chkdate = models.DateTimeField(verbose_name= 'Cheque date')
    refno = models.CharField(max_length=100, verbose_name= 'Reference number')
    bank_code = models.CharField(max_length=100)
    bank_name = models.CharField(max_length=100, validators=[validate_name])
    ifsc = models.CharField(max_length=100)
    acno = models.CharField(max_length=100, verbose_name= 'Account number')
    