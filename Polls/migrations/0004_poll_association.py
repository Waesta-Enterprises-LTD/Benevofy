# Generated by Django 5.0.6 on 2024-06-17 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Associations', '0005_association_rel_account'),
        ('Polls', '0003_remove_candidate_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='association',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Associations.association'),
        ),
    ]
