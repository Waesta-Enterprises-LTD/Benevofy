# Generated by Django 5.0.6 on 2024-06-23 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0008_event_event_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='minimum_contribution_kes',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]