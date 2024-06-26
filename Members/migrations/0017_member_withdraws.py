# Generated by Django 5.0.6 on 2024-06-24 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0016_member_suspensions'),
        ('Withdraws', '0002_withdraw_names'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='withdraws',
            field=models.ManyToManyField(blank=True, related_name='member_withdraws', to='Withdraws.withdraw'),
        ),
    ]
