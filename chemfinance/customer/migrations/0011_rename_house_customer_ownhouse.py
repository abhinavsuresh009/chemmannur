# Generated by Django 5.0.4 on 2024-05-11 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_alter_customer_mob_alter_customer_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='house',
            new_name='ownhouse',
        ),
    ]
