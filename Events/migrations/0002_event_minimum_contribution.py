# Generated by Django 5.0.6 on 2024-06-15 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='minimum_contribution',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
