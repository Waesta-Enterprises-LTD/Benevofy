from django.urls import path
from . import views

urlpatterns = [
    path('request_loan/', views.request_loan, name='request_loan'),
    path('view_loan_requests/', views.view_loan_requests, name='view_loan_requests'),
    path('approve_loan_request/<int:request_id>/', views.approve_loan_request, name='approve_loan_request'),
    path('approve_as_guarantor/<str:reference>/<int:member_id>/', views.approve_as_guarantor, name='approve_as_guarantor'),
    path('approved_as_guarantor/', views.approved_as_guarantor, name='approved_as_guarantor'),
]

