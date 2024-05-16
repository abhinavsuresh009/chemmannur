# Generated by Django 5.0.4 on 2024-05-16 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0025_rename_name_typeoftransaction_payment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daybook',
            name='bank_acc_no',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='daybook',
            name='bank_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='daybook',
            name='cheque_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='daybook',
            name='cheque_no',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='daybook',
            name='ifsc_code',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]