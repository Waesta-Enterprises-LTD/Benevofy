# Generated by Django 5.0.6 on 2024-06-25 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Budgets', '0001_initial'),
        ('Events', '0012_personalevent_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalevent',
            name='amount_required',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='personalevent',
            name='budget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personal_events', to='Budgets.budget'),
        ),
    ]
