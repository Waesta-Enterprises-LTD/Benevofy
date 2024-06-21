from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Payment(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    contributions = models.ManyToManyField('Contributions.EventContribution')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        try:
            contribution = self.contributions.first()
            return f"{self.user} - {contribution.event}"
        except (ObjectDoesNotExist, AttributeError):
            return f"{self.user} - {self.amount_paid}"


class RegistrationPayment(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    association = models.ForeignKey('Associations.Association', on_delete=models.CASCADE, null=True, blank=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=10, choices=[("Paid", "Paid"), ("Pending", "Pending")], default="Pending")

    def __str__(self):
        return f"{self.user} - {self.amount_paid}"