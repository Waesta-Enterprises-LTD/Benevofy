from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_budgets, name='view_budgets'),
    path('add_item_to_budget/<int:event_id>/', views.add_item_to_budget, name='add_item_to_budget'),
    path('view_budget_items/<int:event_id>/', views.view_budget_items, name='view_budget_items'),
    path('mark_item_as_cleared/<int:item_id>/', views.mark_item_as_cleared, name='mark_item_as_cleared'),
    path('edit_item_in_budget/<int:item_id>/', views.edit_item_in_budget, name='edit_item_in_budget'),
    path('delete_item_from_budget/<int:item_id>/', views.delete_item_from_budget, name='delete_item_from_budget'),
]