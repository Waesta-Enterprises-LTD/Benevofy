# Generated by Django 5.0.6 on 2024-06-16 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0002_poll_status_alter_poll_created_on'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='picture',
        ),
    ]
