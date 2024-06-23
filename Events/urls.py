from django.urls import path
from .views import events, delete_event, update_event, create_event, event_report, close_event, resume_event

urlpatterns = [
    path('events/', events, name='events'),
    path('events/<int:event_id>/update/', update_event, name='update-event'),
    path('events/<int:event_id>/delete/', delete_event, name='delete-event'),
    path('events/create/', create_event, name='create-event'),
    path('events/<int:event_id>/report/', event_report, name='event-report'),
    path('events/<int:event_id>/close/', close_event, name='close-event'),
    path('events/<int:event_id>/resume/', resume_event, name='resume-event'),
]

