# Generated by Django 5.0.4 on 2024-05-29 05:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0047_voucherhead_fk_accountinghead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucherhead',
            name='fk_AccountingHead',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='receiptpayment.accountinghead'),
        ),
    ]
