# Generated by Django 2.1.3 on 2018-12-07 10:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pagla', '0002_restaurant_serial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='serial',
        ),
    ]