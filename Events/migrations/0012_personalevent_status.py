# Generated by Django 5.0.6 on 2024-06-25 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0011_remove_event_events'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalevent',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Closed', 'Closed')], default='Active', max_length=10),
        ),
    ]