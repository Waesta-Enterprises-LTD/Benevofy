from django.contrib import admin
from .models import Loan, LoanRepayment

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')
    search_fields = ('user',)

@admin.register(LoanRepayment)
class LoanRepaymentAdmin(admin.ModelAdmin):
    list_display = ('loan', 'user', 'amount')
    search_fields = ('loan__user', 'user')

