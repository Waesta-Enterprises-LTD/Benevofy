# Generated by Django 5.0.6 on 2024-06-14 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Administrators', '0001_initial'),
        ('Contributions', '0001_initial'),
        ('Events', '0001_initial'),
        ('Members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='associations/')),
                ('loan_interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('admins', models.ManyToManyField(to='Administrators.administrator')),
                ('contributions', models.ManyToManyField(to='Contributions.eventcontribution')),
                ('events', models.ManyToManyField(to='Events.event')),
                ('members', models.ManyToManyField(to='Members.member')),
            ],
        ),
    ]
