# Generated by Django 5.0.6 on 2024-06-17 16:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Associations', '0005_association_rel_account'),
        ('Loans', '0004_loanrepayment_loan_loan_repayments'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='association',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Associations.association'),
        ),
    ]