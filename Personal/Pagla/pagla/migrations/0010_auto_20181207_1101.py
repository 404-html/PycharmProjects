# Generated by Django 2.1.3 on 2018-12-07 11:01

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagla', '0009_auto_20181207_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='mpoly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]