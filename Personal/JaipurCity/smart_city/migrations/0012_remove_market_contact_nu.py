# Generated by Django 2.1.4 on 2018-12-10 04:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smart_city', '0011_market'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='market',
            name='contact_nu',
        ),
    ]