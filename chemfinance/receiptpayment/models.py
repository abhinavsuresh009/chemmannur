from time import timezone
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
    mode = models.CharField(max_length=100, default='')
    
    
class Daybook(CommonFields):    
    # fk_AccountingHead = models.ForeignKey(AccountingHead,on_delete = models.PROTECT)
    hcode = models.CharField(max_length = 50)    
    tr_head = models.CharField(max_length = 50, verbose_name="Account Head Code")
    name = models.CharField(max_length = 100, verbose_name="Party Name")
    code = models.CharField(max_length = 50)
    code_from = models.CharField(max_length = 50)
    credit = models.FloatField()
    debit = models.FloatField()
    voucher_no = models.IntegerField()
    cheque_no = models.CharField(max_length = 50)
    cheque_date = models.DateField()
    bank_name = models.CharField(max_length = 100)
    bank_acc_no = models.CharField(max_length = 50)
    ifse_code = models.CharField(max_length = 100)
    typ = models.CharField(max_length = 10)
    mode = models.CharField(max_length = 50)
    approved = models.BooleanField()
    approvedby = models.CharField(max_length = 50 , blank=True)
    approvedtime = models.DateTimeField(blank=True, null=True)    

    def approve(self, username):
        self.approved = True
        self.approvedby= username
        self.approvedtime = timezone.now()
        self.save()
    
class FingerImage(models.Model):
    fpimg = models.TextField()