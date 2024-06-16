from django.db import models

class Poll(models.Model):
    title = models.CharField(max_length=128)
    candidates = models.ManyToManyField('Candidate', related_name='polls')
    closing_date = models.DateField()
    created_on = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active')

    def __str__(self):
        return self.title



class Candidate(models.Model):
    member = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    votes = models.ManyToManyField('Members.Member', related_name='votes')

    def __str__(self):
        return self.member.user.username