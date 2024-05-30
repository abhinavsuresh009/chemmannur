from django.urls import path
from goldloan.views.goldloan import closed_loans, pending_loan
from goldloan.views.natureofloan import *

urlpatterns = [
    path('closed-loans/', closed_loans),
    path('pending-loan/', pending_loan),
    path('nature-loans/', nature_loans),

]