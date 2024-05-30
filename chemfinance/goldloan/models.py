from django.db import models
from utils.basemodel import CommonFields

# Model for goldloan.

class GoldLoan(CommonFields):
    loanid = models.CharField(max_length = 50 , verbose_name = "Loan Id")
    fk_appid =models.CharField(max_length=50)
    period = models.IntegerField()
    amount = models.FloatField()
    interest_rate = models.FloatField()
    duedate = models.DateTimeField()
    Closed_date = models.DateField(default='1863-01-01')
    closed_rate = models.FloatField()
    status =models.CharField(max_length = 10,default = 'N')
    scheme = models.CharField(max_length = 50)
    gold_rate = models.FloatField()
    closed = models.BooleanField(default=False)
    
    
class NatureOfLoan(models.Model):
    title = models.CharField(max_length=50)