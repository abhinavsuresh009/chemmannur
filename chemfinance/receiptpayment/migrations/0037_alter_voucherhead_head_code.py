# Generated by Django 5.0.4 on 2024-05-25 04:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0036_alter_accountinghead_head_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voucherhead',
            name='head_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receiptpayment.accountinghead', to_field='head_code'),
        ),
    ]