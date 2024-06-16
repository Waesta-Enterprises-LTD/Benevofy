from django.urls import path
from . import views

urlpatterns = [
    path('view_loans/', views.view_loans, name='view_loans'),
    path('apply_for_loan/', views.apply_for_loan, name='apply_for_loan'),
]

