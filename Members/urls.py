from .views import member_dashboard, profile, settings, member_profile, view_members
from django.urls import path


urlpatterns = [
    path('member-dashboard/', member_dashboard, name='member-dashboard'),
    path('profile/', profile, name='profile'),
    path('member-profile/<int:member_id>/', member_profile, name='member-profile'),
    path('members/', view_members, name='members'),
    path('settings/', settings, name='settings'),
]
