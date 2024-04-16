from django.urls import path
from companybranch.views.branch import branch, branch_delete_update
from companybranch.views.company import company, company_delete_update



urlpatterns = [

    path('company/', company, name='company'),
    path('branch/', branch, name='branch'),
    path('branch_delete_update/', branch_delete_update, name='branch_delete_update'),
    path('company_delete_update/', company_delete_update, name='company_delete_update'),


]
