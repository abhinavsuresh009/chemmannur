# Generated by Django 5.0.4 on 2024-05-10 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placecode', '0005_remove_city_country_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country_code',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='city',
            name='state_code',
            field=models.CharField(default='', max_length=50),
        ),
    ]
