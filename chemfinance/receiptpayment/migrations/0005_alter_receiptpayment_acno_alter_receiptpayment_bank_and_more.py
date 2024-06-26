# Generated by Django 5.0.4 on 2024-04-11 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0004_alter_receiptpayment_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptpayment',
            name='acno',
            field=models.CharField(max_length=100, verbose_name='Account number'),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='bank',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='chkno',
            field=models.CharField(max_length=100, verbose_name='Check number'),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='hcode',
            field=models.CharField(max_length=100, verbose_name='Head code'),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='hcode1',
            field=models.CharField(max_length=100, verbose_name='Sub head'),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='ifsc',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='mode',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='type',
            field=models.CharField(max_length=100),
        ),
    ]
