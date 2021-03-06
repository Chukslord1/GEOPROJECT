# Generated by Django 2.2.4 on 2020-11-11 01:16

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('APP', '0002_auto_20201110_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geo_location', django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('geo_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.DeleteModel(
            name='Constituency',
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]
