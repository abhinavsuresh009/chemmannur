# Generated by Django 5.0.4 on 2024-04-13 11:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companybranch', '0002_alter_branch_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='brname',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Name must contain only alphabetic characters and cannot start or end with spaces.', regex='^[^\\s].+[a-zA-Z]+[a-zA-Z]+$')], verbose_name='Branch name'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits.', regex='^\\d{10}$')]),
        ),
        migrations.AlterField(
            model_name='company',
            name='comcode',
            field=models.CharField(max_length=20, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Company code cannot contain special characters', regex='^[^\\s].+[a-zA-Z0-9]+[a-zA-Z0-9]+$')], verbose_name='Company code'),
        ),
        migrations.AlterField(
            model_name='company',
            name='comname',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(code='invalid_name', message='Name must contain only alphabetic characters and cannot start or end with spaces.', regex='^[^\\s].+[a-zA-Z]+[a-zA-Z]+$')], verbose_name='Company name'),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Phone number must be 10 digits.', regex='^\\d{10}$')]),
        ),
    ]