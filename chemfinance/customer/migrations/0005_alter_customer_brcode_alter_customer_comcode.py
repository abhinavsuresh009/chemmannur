# Generated by Django 5.0.4 on 2024-04-16 05:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customer_brcode_alter_customer_comcode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='brcode',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Field cannot contain special characters', regex='[a-zA-Z0-9]+$')], verbose_name='Branch Code'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='comcode',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Field cannot contain special characters', regex='[a-zA-Z0-9]+$')], verbose_name='Company Code'),
        ),
    ]