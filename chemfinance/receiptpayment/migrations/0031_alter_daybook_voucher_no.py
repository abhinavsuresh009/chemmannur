# Generated by Django 5.0.4 on 2024-05-23 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0030_alter_daybook_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daybook',
            name='voucher_no',
            field=models.IntegerField(unique=True),
        ),
    ]
