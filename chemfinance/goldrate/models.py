from django.db import models
from utils.basemodel import CommonFields

# Create your models here.

class GoldRate(CommonFields):
    
    rate = models.FloatField(default=0)
    date = models.DateTimeField()