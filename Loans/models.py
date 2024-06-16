from django.db import models

class Loan(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    guarantors = models.ManyToManyField('Members.Member', related_name='loan_guarantors', blank=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='pending')
    repayment_date = models.DateField(null=True, blank=True)
    repaid_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.amount} - {self.status}"
