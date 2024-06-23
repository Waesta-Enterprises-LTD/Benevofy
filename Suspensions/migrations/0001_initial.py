# Generated by Django 5.0.6 on 2024-06-23 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Associations', '0013_association_registration_code_paid'),
        ('Members', '0015_remove_member_is_admin_member_registered_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suspension',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField(max_length=1000)),
                ('from_date', models.DateTimeField(auto_now_add=True)),
                ('till', models.DateField()),
                ('association', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Associations.association')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Members.member')),
            ],
        ),
    ]
