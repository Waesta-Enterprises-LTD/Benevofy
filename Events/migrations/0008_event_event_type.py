# Generated by Django 5.0.6 on 2024-06-18 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0007_event_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(blank=True, choices=[('Administrative', 'Administrative'), ('Condolences', 'Condolences'), ('Medical', 'Medical')], max_length=100, null=True),
        ),
    ]
