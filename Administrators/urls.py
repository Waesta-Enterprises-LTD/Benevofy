from django.urls import path
from . import views


urlpatterns = [
    path('view-administrators/', views.view_administrators, name='administrators'),
    path('assign-admin/<int:member_id>/', views.assign_admin, name='assign-admin'),
    path('revoke-admin/<int:member_id>/', views.revoke_admin, name='revoke-admin'),
]