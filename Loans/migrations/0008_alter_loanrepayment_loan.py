# Generated by Django 5.0.6 on 2024-06-17 17:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loans', '0007_alter_loanrepayment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanrepayment',
            name='loan',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='repayments', to='Loans.loan'),
        ),
    ]