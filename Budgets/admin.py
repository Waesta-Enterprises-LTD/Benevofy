from django.contrib import admin
from .models import Budget, Item

@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('event', 'total_amount')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin): 
    list_display = ('name', 'price', 'cleared')
    list_editable = ('price', 'cleared')