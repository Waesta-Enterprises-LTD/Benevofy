# Generated by Django 5.0.6 on 2024-06-18 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Associations', '0005_association_rel_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='association',
            name='logo',
            field=models.ImageField(upload_to='Associations/logos'),
        ),
    ]
