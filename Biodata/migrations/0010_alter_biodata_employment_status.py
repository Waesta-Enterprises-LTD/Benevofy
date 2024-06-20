# Generated by Django 5.0.6 on 2024-06-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biodata', '0009_alter_dependent_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodata',
            name='employment_status',
            field=models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Self-Employed', 'Self-Employed')], max_length=100, null=True),
        ),
    ]