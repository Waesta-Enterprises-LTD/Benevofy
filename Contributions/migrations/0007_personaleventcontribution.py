# Generated by Django 5.0.6 on 2024-06-25 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contributions', '0006_eventcontribution_method'),
        ('Events', '0013_personalevent_amount_required_personalevent_budget'),
        ('Members', '0019_member_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonalEventContribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(blank=True, max_length=500, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('currency', models.CharField(blank=True, choices=[('UGX', 'UGX'), ('KES', 'KES')], max_length=4, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Paid', 'Paid')], default='Pending', max_length=20)),
                ('method', models.CharField(blank=True, choices=[('Mobile', 'Mobile'), ('Manual', 'Manual')], default='Mobile', max_length=20, null=True)),
                ('personal_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.personalevent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Members.member')),
            ],
        ),
    ]
