# Generated by Django 5.0.6 on 2024-06-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Biodata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='company_or_business',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='employment_status',
            field=models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Employer', 'Employer')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='job_title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='nationality',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='next_of_kin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='next_of_kin_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='next_of_kin_contact',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='work_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='biodata',
            name='work_contact',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='dependent',
            name='relationship',
            field=models.CharField(blank=True, choices=[('Spouse', 'Spouse'), ('Child', 'Child'), ('Sibling', 'Sibling'), ('Parent', 'Parent'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]
