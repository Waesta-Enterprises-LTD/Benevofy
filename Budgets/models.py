from django.db import models

class Budget(models.Model):
    event = models.ForeignKey('Events.PersonalEvent', on_delete=models.CASCADE, null=True,
                              related_name='budgets_set')
    items = models.ManyToManyField('Budgets.Item', blank=True,
                                   related_name='budgets_set')


    def total_amount(self):
        return sum(item.price for item in self.items.all())


class Item(models.Model):
    budget = models.ForeignKey('Budgets.Budget', on_delete=models.CASCADE, null=True,
                               related_name='items_set')
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    cleared = models.BooleanField(default=False)


    def __str__(self): 
        return self.name

    def edit_form(self):
        from .forms import ItemForm
        return ItemForm(instance=self)

