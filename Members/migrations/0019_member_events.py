# Generated by Django 5.0.6 on 2024-06-25 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0011_remove_event_events'),
        ('Members', '0018_alter_member_current_mode'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='events',
            field=models.ManyToManyField(blank=True, related_name='events', to='Events.personalevent'),
        ),
    ]
