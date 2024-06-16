from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    association = models.ForeignKey(
        'Associations.Association',
        on_delete=models.SET_NULL,
        null=True,
        related_name='events_associated',
    )
    minimum_contribution = models.IntegerField(null=True, blank=True)
    contributions = models.ManyToManyField('Contributions.EventContribution', blank=True, related_name='event_contributions')
    closing_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


