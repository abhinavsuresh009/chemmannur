# Generated by Django 5.0.4 on 2024-05-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0021_alter_daybook_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daybook',
            name='credit',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='daybook',
            name='debit',
            field=models.FloatField(default=0),
        ),
    ]
