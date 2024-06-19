from django.contrib import admin
from .models import LoanRequest

@admin.register(LoanRequest)
class LoanRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('user__user_id', 'user__first_name', 'user__last_name')

