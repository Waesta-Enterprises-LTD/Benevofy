from django.urls import path
from . import views

urlpatterns = [
    path('save_money/', views.save_money, name='save_money'),
    path('create_saving_target/', views.create_saving_target, name='create_saving_target'),
    path('view_savings/', views.view_savings, name='view_savings'),
]
