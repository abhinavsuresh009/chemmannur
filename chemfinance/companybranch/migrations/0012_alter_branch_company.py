# Generated by Django 5.0.4 on 2024-04-17 10:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companybranch', '0011_alter_branch_unique_together_alter_branch_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='company',
            field=models.ForeignKey(db_column='comcode', on_delete=django.db.models.deletion.CASCADE, to='companybranch.company', to_field='comcode'),
        ),
    ]
