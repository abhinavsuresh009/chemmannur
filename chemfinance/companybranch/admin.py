from django.contrib import admin
from .models import Company, Branch
# Register your models here.


# class Useredit(admin.ModelAdmin):               
#     search_fields = ['company']
#     list_display = ('brname', 'address')
#     list_filter=('brname','brcode','company') 

admin.site.register(Company)
admin.site.register(Branch)
