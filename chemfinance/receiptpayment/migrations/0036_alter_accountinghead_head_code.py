# Generated by Django 5.0.4 on 2024-05-25 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0035_voucherhead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountinghead',
            name='head_code',
            field=models.CharField(max_length=50, unique=True, verbose_name='Account Head Code'),
        ),
    ]