# Generated by Django 2.2.4 on 2020-11-11 02:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APP', '0007_auto_20201111_0306'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='School',
            new_name='UserProfile',
        ),
        migrations.AlterModelManagers(
            name='userprofile',
            managers=[
            ],
        ),
    ]
