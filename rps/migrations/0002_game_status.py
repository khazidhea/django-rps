# Generated by Django 3.0.8 on 2020-07-28 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='status',
            field=models.CharField(choices=[('created', 'created'), ('started', 'started')], default='created', max_length=20),
        ),
    ]
