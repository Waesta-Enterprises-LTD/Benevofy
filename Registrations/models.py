from django.db import models

class MemberRegistration(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)
    registration_code = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.user} - {self.registration_code}"