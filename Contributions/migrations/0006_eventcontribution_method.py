# Generated by Django 5.0.6 on 2024-06-23 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contributions', '0005_eventcontribution_currency_eventcontribution_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventcontribution',
            name='method',
            field=models.CharField(blank=True, choices=[('Mobile', 'Mobile'), ('Manual', 'Manual')], default='Mobile', max_length=20, null=True),
        ),
    ]
