# Generated by Django 5.0.6 on 2024-06-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0006_event_contributions'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=10),
        ),
    ]
