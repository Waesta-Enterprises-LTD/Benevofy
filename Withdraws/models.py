from django.db import models

class Withdraw(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    association = models.ForeignKey('Associations.Association', on_delete=models.CASCADE, null=True)
    names = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=(('Pending', 'Pending'), ('Successful', 'Successful')), default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user