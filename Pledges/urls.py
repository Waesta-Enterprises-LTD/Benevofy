from django.urls import path
from .views import view_pledges, pledge


urlpatterns = [
    path('view_pledges/<int:event_id>/', view_pledges, name='view_pledges'),
    path('pledge/<int:event_id>/', pledge, name='pledge'),
]