from django.urls import path
from .views import payment_initiated, webhook_receiver


urlpatterns = [
    path('payment_initiated/', payment_initiated, name='payment_initiated'),
    path('webhook_receiver/', webhook_receiver, name='webhook_receiver'),
]  