from django.db import models
from django.contrib import admin
from .models import Loan

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')
    search_fields = ('user',)

    class Meta:
        model = Loan

