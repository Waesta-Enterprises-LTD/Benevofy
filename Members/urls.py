from .views import member_dashboard, profile, settings, member_profile, view_members, generate_id_card
from django.urls import path


urlpatterns = [
    path('member-dashboard/', member_dashboard, name='member-dashboard'),
    path('profile/', profile, name='profile'),
    path('member-profile/<int:member_id>/', member_profile, name='member-profile'),
    path('members/', view_members, name='members'),
    path('generate-id-card/', generate_id_card, name='generate-id-card'),
    path('settings/', settings, name='settings'),
]
