# Generated by Django 5.0.6 on 2024-06-18 10:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Members', '0011_member_verification_code'),
        ('Polls', '0006_poll_agm_attendees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constitution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='poll',
            name='poll_type',
            field=models.CharField(choices=[('Constitutional', 'Constitutional'), ('Electoral', 'Electoral')], default='Electoral', max_length=20),
        ),
        migrations.AddField(
            model_name='poll',
            name='constitution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Polls.constitution'),
        ),
        migrations.CreateModel(
            name='ConstitutionalVote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('Neutral', 'Neutral')], max_length=10)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Members.member')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Polls.poll')),
            ],
        ),
        migrations.AddField(
            model_name='constitution',
            name='votes',
            field=models.ManyToManyField(related_name='constitutions', to='Polls.constitutionalvote'),
        ),
    ]
