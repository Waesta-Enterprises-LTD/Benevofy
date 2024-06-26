from django.contrib import admin
from .models import Event, PersonalEvent

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'closing_date', 'created_at')


@admin.register(PersonalEvent)
class PersonalEventAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_date')

