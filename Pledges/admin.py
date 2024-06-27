from django.contrib import admin
from .models import Pledge

@admin.register(Pledge)
class PledgeAdmin(admin.ModelAdmin):
    list_display = ('names', 'email', 'phone', 'event', 'amount', 'due_date', 'created_at', 'status')
    list_filter = ('event', 'status')
    search_fields = ('names', 'email', 'phone', 'event')
    
