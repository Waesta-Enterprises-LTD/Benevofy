# Generated by Django 5.0.6 on 2024-06-19 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Members', '0012_member_current_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biodata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='biodata_member', to='Members.member')),
            ],
        ),
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relationship', models.CharField(max_length=100)),
                ('biodata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Biodata.biodata')),
                ('dependent_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependent_to', to='Members.member')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dependents', to='Members.member')),
            ],
        ),
        migrations.AddField(
            model_name='biodata',
            name='dependents',
            field=models.ManyToManyField(related_name='parents', through='Biodata.Dependent', to='Members.member'),
        ),
    ]
