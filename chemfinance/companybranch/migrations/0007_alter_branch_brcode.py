# Generated by Django 5.0.4 on 2024-04-17 05:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companybranch', '0006_alter_branch_brcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='brcode',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Company code cannot contain special characters', regex='[a-zA-Z0-9]+$')], verbose_name='Branch code'),
        ),
    ]
