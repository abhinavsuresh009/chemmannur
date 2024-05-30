from time import timezone
from django.db import models
from utils.basemodel import CommonFields
from django.core.validators import RegexValidator
import uuid
from datetime import datetime
import random

# Create your models here.
validate_name = RegexValidator(
    regex='[a-zA-Z0-9]+$',
    message='Name must contain only alphabetic characters',
    code='invalid_name'
)
class ReceiptPayment(CommonFields):
    TRANSACTION_TYPES = (
        ('P', 'P'),
        ('R', 'R'),
    )  
    hcode = models.CharField( max_length=100, verbose_name='Head code')
    hcode1 = models.CharField( max_length=100, verbose_name='Sub head')
    name = models.CharField(max_length=100, validators=[validate_name])
    code = models.CharField(max_length=100)
    credit = models.FloatField(default=0)
    debit = models.FloatField(default=0)    
    vono = models.BigIntegerField(verbose_name='Voucher number')
    type = models.CharField(max_length=100, choices= TRANSACTION_TYPES)
    chkdate = models.DateTimeField(verbose_name='Cheque date')
    chkno = models.CharField(max_length=100, verbose_name='Cheque number')
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
    mode = models.CharField(max_length=100, default='')

class AccountingHead(CommonFields): 
    # fk_grouphead = models.ForeignKey(GroupHead,on_delete = models.PROTECT)
    head_code = models.CharField(max_length = 50, verbose_name="Account Head Code")      
    grouphead_id = models.CharField(max_length = 100, verbose_name="Group head id")    
    name = models.CharField(max_length = 100, verbose_name="head Name")  
    
class Daybook(CommonFields):   
    fk_AccountingHead = models.ForeignKey(AccountingHead,on_delete = models.PROTECT)
    hcode = models.CharField(max_length = 50)    
    tr_head = models.CharField(max_length = 50, verbose_name="Account Head Code", blank=True)
    name = models.CharField(max_length = 100, verbose_name="Party Name", blank=True)
    code = models.CharField(max_length = 50, blank=True)
    code_from = models.CharField(max_length = 50, blank=True)
    credit = models.FloatField(default=0)
    debit = models.FloatField(default=0)
    voucher_no = models.IntegerField(unique = True)
    cheque_no = models.CharField(max_length = 50, blank=True)
    cheque_date = models.DateField(blank=True, null=True)
    bank_name = models.CharField(max_length = 100, blank=True)
    bank_acc_no = models.CharField(max_length = 50, blank=True)
    ifsc_code = models.CharField(max_length = 100, blank=True)
    type = models.CharField(max_length=100)    
    mode = models.CharField(max_length = 50)
    approved = models.BooleanField(default=False)
    approvedby = models.CharField(max_length = 50 , blank=True)
    approvedtime = models.DateTimeField(blank=True, null=True)    
    
    
    
class FingerImage(models.Model):
    fpimg = models.TextField()
    
class TypeOfTransaction(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    payment_name = models.CharField(max_length=50, unique=True)
    
    
class VoucherHead(CommonFields):
    fk_AccountingHead = models.ForeignKey(AccountingHead,on_delete = models.PROTECT)
    head_code = models.CharField(max_length=50)
