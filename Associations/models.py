from django.db import models
from uuid import uuid4


class Association(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='Associations/logos')
    rel_account = models.CharField(max_length=100, null=True, blank=True)
    members = models.ManyToManyField('Members.Member', blank=True)
    contributions = models.ManyToManyField('Contributions.EventContribution', blank=True)
    admins = models.ManyToManyField('Administrators.Administrator', blank=True)
    events = models.ManyToManyField('Events.Event',
                                   related_name='associated_events', blank=True)
    loan_interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    registration_code = models.UUIDField(default=uuid4)

    def __str__(self):
        return self.name

