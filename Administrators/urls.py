from django.urls import path
from . import views


urlpatterns = [
    path('view-administrators/', views.view_administrators, name='administrators'),
]