# Generated by Django 5.0.4 on 2024-04-12 05:08

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0007_alter_receiptpayment_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('gcode', models.CharField(max_length=50, verbose_name='Group Code')),
                ('comcode', models.CharField(max_length=50, verbose_name='Company Code')),
                ('brcode', models.CharField(max_length=50, verbose_name='Branch Code')),
                ('ucode', models.CharField(max_length=50, verbose_name='User Code')),
                ('trdate', models.DateTimeField(auto_now_add=True, verbose_name='Transation Date')),
                ('description', models.TextField(blank=True)),
                ('hcode', models.CharField(max_length=100, verbose_name='Head code')),
                ('hcode1', models.CharField(max_length=100, verbose_name='Sub name')),
                ('party_name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=100)),
                ('credit', models.FloatField(default=0)),
                ('debit', models.FloatField(default=0)),
                ('chkdate', models.DateTimeField(verbose_name='Cheque date')),
                ('refno', models.CharField(max_length=100, verbose_name='Reference number')),
                ('bank_code', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('ifsc', models.CharField(max_length=100)),
                ('acno', models.CharField(max_length=100, verbose_name='Account number')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]