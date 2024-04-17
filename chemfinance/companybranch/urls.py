from django.urls import path
from companybranch.views.branch import *
from companybranch.views.company import *



urlpatterns = [

    path('company/', company, name='company'),
    path('branch/<str:comcode>/', branch, name='branch'),
    path('create_branch/', create_branch, name='create_branch'),
    path('branch_delete_update/', branch_delete_update, name='branch_delete_update'),
    path('company_delete_update/', company_delete_update, name='company_delete_update'),


]
