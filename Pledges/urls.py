from django.urls import path
from .views import view_pledges, pledge, delete_pledge, mark_paid, paid_card


urlpatterns = [
    path('view_pledges/<int:event_id>/', view_pledges, name='view_pledges'),
    path('pledge/<int:event_id>/', pledge, name='pledge'),
    path('delete_pledge/<int:pledge_id>/', delete_pledge, name='delete_pledge'),
    path('mark_paid/<int:pledge_id>/', mark_paid, name='mark_paid'),
    path('paid_card/<int:pledge_id>/', paid_card, name='paid_card'),
]