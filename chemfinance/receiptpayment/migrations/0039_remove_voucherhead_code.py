# Generated by Django 5.0.4 on 2024-05-25 05:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0038_alter_accountinghead_head_code_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voucherhead',
            name='code',
        ),
    ]