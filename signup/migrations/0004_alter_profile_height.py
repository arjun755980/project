# Generated by Django 5.0.6 on 2024-06-15 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0003_profile_mother_tounge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
