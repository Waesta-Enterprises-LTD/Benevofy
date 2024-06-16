# Generated by Django 5.0.6 on 2024-06-16 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0004_remove_event_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AddField(
            model_name='event',
            name='closing_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
