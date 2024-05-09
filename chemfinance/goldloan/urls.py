from django.urls import path
from goldloan.views.goldloan import closed_loans, pending_loan

urlpatterns = [
    path('closed-loans/', closed_loans),
    path('pending-loan/', pending_loan),

]