# Generated by Django 4.0.3 on 2022-05-18 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_location_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='username',
            new_name='description',
        ),
    ]
