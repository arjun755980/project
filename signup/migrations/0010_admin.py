# Generated by Django 5.0.6 on 2024-10-13 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0009_rename_mother_tounge_profile_mother_tongue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=100, unique=True)),
                ('password', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
