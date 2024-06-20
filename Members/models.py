from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biodata = models.OneToOneField(
        'Biodata.Biodata',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='member_biodata'
    )
    email_verified = models.BooleanField(default=False)
    verification_code = models.CharField(max_length=500, null=True, blank=True)
    current_mode = models.CharField(max_length=10, choices=[("Member", "Member"), ("Admin", "Admin")], default="Member")
    picture = models.ImageField(upload_to='Members/profile_pictures/', null=True, blank=True)
    associations = models.ManyToManyField('Associations.Association', blank=True, related_name='member_associations')
    contributions = models.ManyToManyField('Contributions.EventContribution', blank=True, related_name='member_contributions')
    savings = models.ManyToManyField('Savings.Saving', blank=True, related_name='member_savings')
    logged_in_association = models.ForeignKey('Associations.Association', on_delete=models.SET_NULL, null=True, blank=True, related_name='member_logged_in')
    phone = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female")], null=True, blank=True)
    declaration = models.TextField(max_length=1000 ,null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def savings_total(self):
        total = 0
        for savings in self.savings.filter(status='Paid'):
            total += savings.amount
        return total



