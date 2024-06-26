# Generated by Django 5.0.6 on 2024-06-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Savings', '0005_savingtarget_savings'),
    ]

    operations = [
        migrations.AddField(
            model_name='saving',
            name='reference',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='saving',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending', max_length=20),
        ),
    ]
