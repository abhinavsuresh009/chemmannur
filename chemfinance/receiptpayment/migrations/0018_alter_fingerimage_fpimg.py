# Generated by Django 5.0.4 on 2024-05-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receiptpayment', '0017_fingerimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fingerimage',
            name='fpimg',
            field=models.TextField(),
        ),
    ]