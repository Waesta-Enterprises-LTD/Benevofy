from django.contrib import admin
from .models import Association

@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo', 'loan_interest_rate']
    list_filter = ['name']
    search_fields = ['name']
    filter_horizontal = ['members', 'contributions', 'admins', 'events']


