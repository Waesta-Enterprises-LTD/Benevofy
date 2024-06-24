from django.urls import path
from .views import view_withdraws


urlpatterns = [
    path('view_withdraws/', view_withdraws, name='view_withdraws'),
]