# Generated by Django 5.0.4 on 2024-05-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placecode', '0006_city_country_code_city_state_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='country_code',
            field=models.CharField(default='', max_length=50),
        ),
    ]
