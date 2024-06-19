from django.db import models

class LoanRequest(models.Model):
    association = models.ForeignKey('Associations.Association', on_delete=models.CASCADE)
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    recieving_number = models.BigIntegerField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    guarantors = models.ManyToManyField('Members.Member', related_name='loan_request_guarantors', blank=True)
    approved_guarantors = models.ManyToManyField('Members.Member', related_name='loan_request_approved_guarantors', blank=True)
    applied_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    status = models.CharField(max_length=50, default='waiting for guarantors', choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('waiting for guarantors', 'Waiting for guarantors'),
    ])
    repayment_date = models.DateField(null=True, blank=True)
    loan = models.OneToOneField('Loans.Loan', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.amount} - {self.status}"