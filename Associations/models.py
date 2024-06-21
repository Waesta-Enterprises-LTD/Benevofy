from django.db import models
from uuid import uuid4


class Association(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    website = models.URLField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    logo = models.ImageField(upload_to='Associations/logos')
    rel_account = models.CharField(max_length=100, null=True, blank=True)
    members = models.ManyToManyField('Members.Member', blank=True, related_name='member_associations')
    contributions = models.ManyToManyField('Contributions.EventContribution', blank=True)
    admins = models.ManyToManyField('Members.Member', blank=True, related_name='admin_associations')
    savings = models.ManyToManyField('Savings.NormalSaving', blank=True, related_name='associations')
    events = models.ManyToManyField('Events.Event',
                                   related_name='associated_events', blank=True)
    loan_interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    registration_code = models.UUIDField(default=uuid4)
    minimum_monthly_savings = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    registration_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.name

