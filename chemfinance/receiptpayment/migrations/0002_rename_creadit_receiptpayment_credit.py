# Generated by Django 5.0.4 on 2024-04-11 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='receiptpayment',
            old_name='creadit',
            new_name='credit',
        ),
    ]
