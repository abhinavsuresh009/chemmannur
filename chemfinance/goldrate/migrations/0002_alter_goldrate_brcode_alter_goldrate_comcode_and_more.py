# Generated by Django 5.0.4 on 2024-04-15 15:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goldrate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goldrate',
            name='brcode',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Field cannot contain special characters', regex='[a-zA-Z0-9]$')], verbose_name='Branch Code'),
        ),
        migrations.AlterField(
            model_name='goldrate',
            name='comcode',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Field cannot contain special characters', regex='[a-zA-Z0-9]$')], verbose_name='Company Code'),
        ),
        migrations.AlterField(
            model_name='goldrate',
            name='gcode',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Field cannot contain special characters', regex='[a-zA-Z0-9]$')], verbose_name='Group Code'),
        ),
        migrations.AlterField(
            model_name='goldrate',
            name='ucode',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Field cannot contain special characters', regex='[a-zA-Z0-9]$')], verbose_name='User Code'),
        ),
    ]
