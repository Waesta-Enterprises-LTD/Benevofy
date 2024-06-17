from django.db import models
from django.contrib import admin
from .models import Saving, SavingTarget

@admin.register(Saving)
class SavingAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'status', 'reference', 'created_at')
    search_fields = ['user__first_name', 'user__last_name']

@admin.register(SavingTarget)
class SavingTargetAdmin(admin.ModelAdmin):
    list_display = ('target_name', 'amount', 'progress', 'created_at')
    search_fields = ['target_name', 'user__first_name', 'user__last_name']

