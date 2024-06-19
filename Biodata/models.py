from django.db import models

class Biodata(models.Model):
    member = models.OneToOneField('Members.Member', on_delete=models.CASCADE, related_name='biodata_member')
    address = models.TextField()
    dependents = models.ManyToManyField('Members.Member', through='Dependent',
                                       through_fields=('biodata', 'dependent_to'), related_name='parents')


class Dependent(models.Model):
    member = models.ForeignKey('Members.Member', on_delete=models.CASCADE, related_name='dependents')
    dependent_to = models.ForeignKey('Members.Member', on_delete=models.CASCADE, related_name='dependent_to')
    biodata = models.ForeignKey('Biodata', on_delete=models.CASCADE)
    relationship = models.CharField(max_length=100)

