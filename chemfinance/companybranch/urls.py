from django.urls import path
from companybranch.views.branch import branch
from companybranch.views.company import company



urlpatterns = [

    path('company_list/', company, name='company_list'),
    path('branch_list/', branch, name='branch_list'),


]
