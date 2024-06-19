from django.urls import path
from . import views

urlpatterns = [
    path('view_loans/', views.view_loans, name='view_loans'),
    path('apply_for_loan/', views.apply_for_loan, name='apply_for_loan'),
    path('repay_loan/<int:loan_id>/', views.repay_loan, name='repay_loan'),
    path('loan_payments/<int:loan_id>/', views.loan_payments, name='loan_payments'),
]

