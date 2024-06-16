from django.urls import path
from .views import select_events, pay_for_events, request_to_pay


urlpatterns = [
    path('select_events/', select_events, name='select_events'),
    path('pay_for_events/', pay_for_events, name='pay_for_events'),
    path('request_to_pay/', request_to_pay, name='request_to_pay'),
]