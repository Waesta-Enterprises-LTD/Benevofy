from django.db import models

class Saving(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    target = models.ForeignKey('Savings.SavingTarget', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.amount}"



class SavingTarget(models.Model):
    target_name = models.CharField(max_length=100)
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    progress = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.amount}"