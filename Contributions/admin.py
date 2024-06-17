from django.db import models
from django.contrib import admin
from .models import EventContribution

@admin.register(EventContribution)
class EventContributionAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'reference', 'amount', 'created_at', 'status')
    list_filter = ('status',)
    search_fields = ('user__first_name', 'user__last_name', 'event__title')
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

