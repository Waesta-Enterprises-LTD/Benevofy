# Generated by Django 5.0.6 on 2024-06-15 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10, null=True),
        ),
    ]
