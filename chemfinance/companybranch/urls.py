from django.urls import path
from companybranch.views.branch import *
from companybranch.views.company import *



urlpatterns = [

    path('company/', company, name='company'),
    path('company-details/<str:comcode>/', company_details, name='company_details'),
    path('branch/<str:comcode>/', branch, name='branch'),
    path('branches/<str:comcode>/', branches, name='branches'),
    path('create-branch/', create_branch, name='create-branch'),
    path('branch-delete-update/', branch_delete_update, name='branch-delete-update'),
    path('company-delete-update/', company_delete_update, name='company-delete-update'),


]
# urls.py



