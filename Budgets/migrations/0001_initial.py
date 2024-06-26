# Generated by Django 5.0.6 on 2024-06-25 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Events', '0012_personalevent_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='budgets_set', to='Events.personalevent')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('budget', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items_set', to='Budgets.budget')),
            ],
        ),
        migrations.AddField(
            model_name='budget',
            name='items',
            field=models.ManyToManyField(blank=True, related_name='budgets_set', to='Budgets.item'),
        ),
    ]
