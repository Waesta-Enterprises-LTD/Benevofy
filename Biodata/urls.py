from django.urls import path
from . import views

urlpatterns = [
    path('biodata/', views.biodata, name='biodata'),
]