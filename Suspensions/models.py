from django.db import models

class Suspension(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    association = models.ForeignKey('Associations.Association', on_delete=models.CASCADE, null=True)
    reason = models.TextField(max_length=1000)
    from_date = models.DateTimeField(auto_now_add=True)
    till = models.DateField()
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Ended', 'Ended')], default='Active')

    def __str__(self):
        return self.reason