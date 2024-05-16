# Generated by Django 5.0.4 on 2024-05-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0018_alter_fingerimage_fpimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptpayment',
            name='chkdate',
            field=models.DateTimeField(verbose_name='Cheque date'),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='chkno',
            field=models.CharField(max_length=100, verbose_name='Cheque number'),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='type',
            field=models.CharField(choices=[('P', 'P'), ('R', 'R')], max_length=100),
        ),
    ]
