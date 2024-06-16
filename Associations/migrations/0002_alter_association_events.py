# Generated by Django 5.0.6 on 2024-06-15 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Associations', '0001_initial'),
        ('Events', '0002_event_minimum_contribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='events',
            field=models.ManyToManyField(related_name='associated_events', to='Events.event'),
        ),
    ]
