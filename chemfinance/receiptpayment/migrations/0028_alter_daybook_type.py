# Generated by Django 5.0.4 on 2024-05-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0027_alter_daybook_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daybook',
            name='type',
            field=models.CharField(choices=[('P', 'P'), ('R', 'R')], max_length=100),
        ),
    ]
