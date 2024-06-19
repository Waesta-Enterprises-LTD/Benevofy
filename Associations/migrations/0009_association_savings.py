# Generated by Django 5.0.6 on 2024-06-19 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Associations', '0008_alter_association_admins_alter_association_members'),
        ('Savings', '0008_normalsaving'),
    ]

    operations = [
        migrations.AddField(
            model_name='association',
            name='savings',
            field=models.ManyToManyField(blank=True, related_name='associations', to='Savings.normalsaving'),
        ),
    ]
