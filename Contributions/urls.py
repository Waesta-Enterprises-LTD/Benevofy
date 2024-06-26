from django.urls import path
from .views import select_events, pay_for_events, request_to_pay, select_member_to_pay, contribute_to_personal_event


urlpatterns = [
    path('select_events/<int:member_id>/', select_events, name='select_events'),
    path('pay_for_events/', pay_for_events, name='pay_for_events'),
    path('request_to_pay/', request_to_pay, name='request_to_pay'),
    path('select_member_to_pay/', select_member_to_pay, name='select_member_to_pay'),
    path('contribute/<int:event_id>/', contribute_to_personal_event, name='contribute_to_personal_event'),
]