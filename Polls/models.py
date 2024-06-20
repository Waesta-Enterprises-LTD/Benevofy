from django.db import models

class Poll(models.Model):
    association = models.ForeignKey('Associations.Association', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=128)
    candidates = models.ManyToManyField('Candidate', related_name='polls')
    closing_date = models.DateField()
    created_on = models.DateField(auto_now_add=True)
    constitution = models.ForeignKey('Polls.Constitution', on_delete=models.SET_NULL, null=True)
    poll_type = models.CharField(max_length=20, choices=[('Constitutional', 'Constitutional'), ('Electoral', 'Electoral')], default='Electoral')
    voters = models.ManyToManyField('Members.Member', related_name='polls')
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active')
    agm_attendees = models.ManyToManyField('Members.Member', related_name='agm_polls', blank=True)

    def __str__(self):
        return self.title



class Candidate(models.Model):
    poll = models.ForeignKey('Polls.Poll', on_delete=models.SET_NULL, null=True)
    member = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    votes = models.ManyToManyField('Members.Member', related_name='votes')

    def __str__(self):
        return self.member.user.username


class Constitution(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    votes = models.ManyToManyField('ConstitutionalVote', related_name='constitutions')


    def __str__(self):
        return self.title


class ConstitutionalVote(models.Model):
    poll = models.ForeignKey('Polls.Poll', on_delete=models.CASCADE)
    member = models.ForeignKey('Members.Member', on_delete=models.CASCADE)
    vote = models.CharField(max_length=10, choices=[('Yes', 'Yes'), ('No', 'No'), ('Neutral', 'Neutral')])