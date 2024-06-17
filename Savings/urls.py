from django.urls import path
from . import views

urlpatterns = [
    path('save_money/', views.save_money, name='save_money'),
    path('create_saving_target/', views.create_saving_target, name='create_saving_target'),
    path('view_savings/', views.view_savings, name='view_savings'),
    path('<int:target_id>/savings/', views.view_target_savings, name='view_target_savings'),
]
