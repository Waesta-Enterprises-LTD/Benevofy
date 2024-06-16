# Generated by Django 5.0.6 on 2024-06-15 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Members', '0006_member_is_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='candidates')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Members.member')),
                ('votes', models.ManyToManyField(related_name='votes', to='Members.member')),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('closing_date', models.DateField()),
                ('created_on', models.DateField()),
                ('candidates', models.ManyToManyField(related_name='polls', to='Polls.candidate')),
            ],
        ),
    ]
