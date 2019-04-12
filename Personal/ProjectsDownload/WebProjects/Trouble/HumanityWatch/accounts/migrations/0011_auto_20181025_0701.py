# Generated by Django 2.1.2 on 2018-10-25 07:01

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20181023_1536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historicaluser',
            old_name='address',
            new_name='first_address',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='address',
            new_name='first_address',
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='phone',
            field=models.CharField(default=django.utils.timezone.now, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='profession',
            field=models.CharField(choices=[('s', 'Student'), ('e', 'Employer'), ('u', 'Unemployed'), ('b', 'Businessman')], default=datetime.datetime(2018, 10, 25, 7, 0, 26, 442127, tzinfo=utc), max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicaluser',
            name='second_address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default=datetime.datetime(2018, 10, 25, 7, 0, 46, 65409, tzinfo=utc), max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='profession',
            field=models.CharField(choices=[('s', 'Student'), ('e', 'Employer'), ('u', 'Unemployed'), ('b', 'Businessman')], default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='second_address',
            field=models.CharField(default='', max_length=255),
        ),
    ]