# Generated by Django 5.0.6 on 2024-06-19 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Associations', '0007_association_minimum_monthly_savings'),
        ('Members', '0013_member_biodata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='admin_associations', to='Members.member'),
        ),
        migrations.AlterField(
            model_name='association',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='member_associations', to='Members.member'),
        ),
    ]
