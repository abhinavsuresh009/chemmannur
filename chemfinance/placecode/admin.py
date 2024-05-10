# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.


# class Useredit(admin.ModelAdmin):               
#     search_fields = ['company']
#     list_display = ('brname', 'address')
#     list_filter=('brname','brcode','company') 

admin.site.register(Country)
admin.site.register(City)
admin.site.register(State)
