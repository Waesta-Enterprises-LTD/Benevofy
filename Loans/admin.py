from django.contrib import admin
from .models import Loan, LoanRepayment

@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'association')
    search_fields = ('user', 'association')

@admin.register(LoanRepayment)
class LoanRepaymentAdmin(admin.ModelAdmin):
    list_display = ('loan', 'user', 'amount', 'payment_date', 'reference', 'status')
    search_fields = ('loan__user', 'user')


