# Generated by Django 5.0.6 on 2024-06-17 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0006_profile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
