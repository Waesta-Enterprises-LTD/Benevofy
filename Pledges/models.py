from django.db import models

class Pledge(models.Model):
    names = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    event = models.ForeignKey('Events.PersonalEvent', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Unpaid', choices=[('Unpaid', 'Unpaid'), ('Paid', 'Paid')])

    def __str__(self):
        return f"{self.email} - {self.event}"