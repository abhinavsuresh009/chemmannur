# Generated by Django 5.0.4 on 2024-05-15 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0022_alter_daybook_credit_alter_daybook_debit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daybook',
            old_name='ifse_code',
            new_name='ifsc_code',
        ),
        migrations.AlterField(
            model_name='daybook',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
