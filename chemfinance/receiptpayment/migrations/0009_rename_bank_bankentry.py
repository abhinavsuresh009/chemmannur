# Generated by Django 5.0.4 on 2024-04-12 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0008_bank'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bank',
            new_name='BankEntry',
        ),
    ]
