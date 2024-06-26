# Generated by Django 5.0.6 on 2024-06-25 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contributions', '0007_personaleventcontribution'),
        ('Events', '0013_personalevent_amount_required_personalevent_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalevent',
            name='contributions',
            field=models.ManyToManyField(blank=True, related_name='personal_event_contributions', to='Contributions.personaleventcontribution'),
        ),
        migrations.AddField(
            model_name='personalevent',
            name='event_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
