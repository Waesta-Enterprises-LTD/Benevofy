from django.db import models
import random

def generate_token():
    return random.randint(100000, 999999)

class PasswordResetToken(models.Model):
    user = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    token = models.IntegerField(default=generate_token)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.token


