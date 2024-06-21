from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import admin
from .models import Payment, RegistrationPayment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount_paid', 'paid_at')

@admin.register(RegistrationPayment)
class RegistrationPaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount_paid', 'paid_at', 'status')


