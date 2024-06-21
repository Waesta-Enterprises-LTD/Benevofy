from django.urls import path
from .views import settings


urlpatterns = [
    path('settings/', settings, name='association-settings'),
]