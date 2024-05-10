from django.db import models
from utils.basemodel import CommonFields
# Create your models here.

class Country(CommonFields):
    country_code = models.CharField(max_length=50, unique=True)
    country_name = models.CharField(max_length=50)
    

class State(CommonFields):
    country = models.ForeignKey(Country,to_field='country_code', on_delete=models.CASCADE)
    state_code = models.CharField(max_length=50)
    state_name = models.CharField(max_length=50)
    
class City(CommonFields):
    state = models.ForeignKey(State,on_delete=models.CASCADE)
    state_code = models.CharField(max_length=50,default='')
    country_code = models.CharField(max_length=50, default='')
    city_code = models.CharField(max_length=50, default='')
    city_name = models.CharField(max_length=50)