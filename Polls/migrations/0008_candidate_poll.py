# Generated by Django 5.0.6 on 2024-06-19 15:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Polls', '0007_constitution_poll_poll_type_poll_constitution_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='poll',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Polls.poll'),
        ),
    ]