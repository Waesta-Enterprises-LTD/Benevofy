# Generated by Django 5.0.6 on 2024-06-20 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Savings', '0010_alter_normalsaving_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='normalsaving',
            name='target',
            field=models.CharField(blank=True, default='Monthly Savings', max_length=100, null=True),
        ),
    ]
