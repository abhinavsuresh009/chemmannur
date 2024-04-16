from django.urls import path
from goldloan.views.goldloan import closed_loans, pending_loan

urlpatterns = [
    path('closed_loans/', closed_loans),
    path('pending_loan/', pending_loan),

]