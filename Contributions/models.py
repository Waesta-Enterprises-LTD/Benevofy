from django.db import models

class EventContribution(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    event = models.ForeignKey('Events.Event', on_delete=models.CASCADE)
    reference = models.CharField(max_length=500, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending', choices=[('Pending', 'Pending'), ('Paid', 'Paid')])

    def __str__(self):
        return f"{self.user} - {self.event}"

