# Generated by Django 5.0.4 on 2024-05-10 06:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_alter_customer_house'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='mob',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Invalid phone number', regex='^\\d{10}$')]),
        ),
    ]
