from django.db import models


event_types = (
    ('Administrative', 'Administrative'),
    ('Condolences', 'Condolences'),
    ('Medical', 'Medical'),
)

personal_event_types = (
    ('Birthday', 'Birthday'),
    ('Anniversary', 'Anniversary'),
    ('Condolences', 'Condolences'),
    ('Wedding', 'Wedding'),
)

class Event(models.Model):
    name = models.CharField(max_length=100)
    association = models.ForeignKey(
        'Associations.Association',
        on_delete=models.SET_NULL,
        null=True,
        related_name='events_associated',
    )
    event_type = models.CharField(max_length=100, choices=event_types, null=True, blank=True)
    minimum_contribution = models.IntegerField(null=True, blank=True)
    minimum_contribution_kes = models.IntegerField(null=True, blank=True)
    contributions = models.ManyToManyField('Contributions.EventContribution', blank=True, related_name='event_contributions')
    closing_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class PersonalEvent(models.Model):
    name = models.CharField(max_length=100)
    amount_required = models.IntegerField(null=True, blank=True)
    budget = models.ForeignKey('Budgets.Budget', on_delete=models.SET_NULL, null=True, blank=True, related_name='personal_events')
    pledges = models.ManyToManyField('Pledges.Pledge', blank=True, related_name='personal_events')
    member = models.ForeignKey(
        'Members.Member',
        on_delete=models.CASCADE,
        related_name='personal_events'
    )
    minimum_contribution = models.IntegerField(null=True, blank=True)
    contributions = models.ManyToManyField('Contributions.PersonalEventContribution', blank=True, related_name='personal_event_contributions')
    event_type = models.CharField(max_length=100, choices=personal_event_types, null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active')