from django.urls import path
from . import views

urlpatterns = [
    path('request_loan/', views.request_loan, name='request_loan'),
]

