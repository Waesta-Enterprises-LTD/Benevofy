from django.db import models
from django.utils import timezone

class Saving(models.Model):
    association = models.ForeignKey('Associations.Association', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    target = models.ForeignKey('Savings.SavingTarget', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending')
    reference = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.amount}"



class SavingTarget(models.Model):
    target_name = models.CharField(max_length=100)
    association = models.ForeignKey('Associations.Association', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    target_date = models.DateField(null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    savings = models.ManyToManyField('Savings.Saving', blank=True)
    progress = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.target_name} - {self.amount}"

    def amount_saved(self):
        return sum(saving.amount for saving in self.savings.all())

    def last_saved_date(self):
        try:
            return self.savings.first().created_at
        except:
            return None



class NormalSaving(models.Model):
    association = models.ForeignKey('Associations.Association', on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    target = models.CharField(max_length=100, null=True, blank=True, default="Monthly Savings")
    date = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reference = models.CharField(max_length=500, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending')

    def __str__(self):
        return f"{self.member} - {self.amount}"