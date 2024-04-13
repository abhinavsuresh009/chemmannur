# Generated by Django 5.0.4 on 2024-04-11 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0002_rename_creadit_receiptpayment_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptpayment',
            name='credit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='debit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receiptpayment',
            name='type',
            field=models.CharField(choices=[('P', 'P'), ('R', 'R')], max_length=80),
        ),
    ]