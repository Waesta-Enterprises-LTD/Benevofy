from django.db import models

class Withdraw(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    association = models.ForeignKey('Associations.Association', on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=(('Pending', 'Pending'), ('Successful', 'Successful')), default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class WithdrawRequest(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    association = models.ForeignKey('Associations.Association', on_delete=models.CASCADE, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100, choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')), default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey('Members.Member', on_delete=models.CASCADE, related_name='withdraw_request_approved_by', null=True, blank=True)

    def __str__(self):
        return self.user