from django.urls import path
from .views import payment_initiated, webhook_receiver, view_paid_list, add_manual_payment, view_personal_paid_list


urlpatterns = [
    path('payment_initiated/', payment_initiated, name='payment_initiated'),
    path('webhook_receiver/', webhook_receiver, name='webhook_receiver'),
    path('view_paid_list/<int:event_id>/', view_paid_list, name='view_paid_list'),
    path('add_manual_payment/<int:event_id>/', add_manual_payment, name='add_manual_payment'),
    path('view_personal_paid_list/<int:event_id>/', view_personal_paid_list, name='view-personal-paid-list'),
]  