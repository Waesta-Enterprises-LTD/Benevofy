from django.db import models

class Loan(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    association = models.ForeignKey('Associations.Association', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    guarantors = models.ManyToManyField('Members.Member', related_name='loan_guarantors', blank=True)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    repayment_date = models.DateField(null=True, blank=True)
    repaid_at = models.DateTimeField(null=True, blank=True)
    loan_repayments = models.ManyToManyField('Loans.LoanRepayment', related_name='loans', blank=True)

    def __str__(self):
        return f"{self.amount} - {self.association} Association"

class LoanRepayment(models.Model):
    loan = models.ForeignKey('Loans.Loan', on_delete=models.SET_NULL, null=True, related_name='repayments')
    user = models.ForeignKey('Members.Member', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    reference = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending')

    def __str__(self):
        return f"{self.user} - {self.amount}"


