# Generated by Django 5.0.6 on 2024-06-24 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0017_member_withdraws'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='current_mode',
            field=models.CharField(choices=[('Member', 'Member'), ('Admin', 'Admin'), ('Personal', 'Personal')], default='Personal', max_length=10),
        ),
    ]
