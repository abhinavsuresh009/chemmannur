# Generated by Django 5.0.4 on 2024-05-29 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0046_alter_daybook_fk_accountinghead'),
    ]

    operations = [
        migrations.AddField(
            model_name='voucherhead',
            name='fk_AccountingHead',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='receiptpayment.accountinghead'),
        ),
    ]
