from django.db import models

class Budget(models.Model):
    event = models.ForeignKey('Events.PersonalEvent', on_delete=models.CASCADE, null=True,
                              related_name='budgets_set')
    items = models.ManyToManyField('Budgets.Item', blank=True,
                                   related_name='budgets_set')


class Item(models.Model):
    budget = models.ForeignKey('Budgets.Budget', on_delete=models.CASCADE, null=True,
                               related_name='items_set')
    name = models.CharField(max_length=100)
    price = models.IntegerField()


    def __str__(self): 
        return self.name

