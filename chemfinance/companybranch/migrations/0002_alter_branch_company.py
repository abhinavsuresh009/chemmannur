# Generated by Django 5.0.4 on 2024-04-13 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companybranch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(db_column='comcode', on_delete=django.db.models.deletion.CASCADE, to='companybranch.company', to_field='comcode'),
        ),
    ]