from django.urls import path
from . import views

urlpatterns = [
    path('save_money/<int:target_id>/', views.save_money, name='save_money'),
    path('create_saving_target/', views.create_saving_target, name='create_saving_target'),
    path('view_savings/', views.view_savings, name='view_savings'),
    path('<int:target_id>/savings/', views.view_target_savings, name='view_target_savings'),
    path('normal_saving/', views.normal_saving, name='normal_saving'),
    path('delete_target/<int:target_id>/', views.delete_target, name='delete_target'),
    path('view_monthly_savings/', views.view_monthly_savings, name='view_monthly_savings'),
]
