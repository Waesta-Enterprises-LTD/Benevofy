from django.urls import path
from .views import events, delete_event, update_event, create_event, event_report, close_event, resume_event, create_personal_event, view_personal_events, delete_personal_event, close_personal_event, resume_personal_event

urlpatterns = [
    path('events/', events, name='events'),
    path('events/<int:event_id>/update/', update_event, name='update-event'),
    path('events/<int:event_id>/delete/', delete_event, name='delete-event'),
    path('events/create/', create_event, name='create-event'),
    path('events/<int:event_id>/report/', event_report, name='event-report'),
    path('events/<int:event_id>/close/', close_event, name='close-event'),
    path('events/<int:event_id>/resume/', resume_event, name='resume-event'),
    path('create-personal-event/', create_personal_event, name='create-personal-event'),
    path('view-personal-events/', view_personal_events, name='view-personal-events'),
    path('delete-personal-event/<int:event_id>/', delete_personal_event, name='delete-personal-event'),
    path('close-personal-event/<int:event_id>/', close_personal_event, name='close-personal-event'),
    path('resume-personal-event/<int:event_id>/', resume_personal_event, name='resume-personal-event'),
]

