# Generated by Django 5.0.4 on 2024-05-27 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0042_remove_voucherhead_head_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daybook',
            name='cheque_date',
            field=models.DateField(blank=True),
        ),
    ]