# Generated by Django 5.0.4 on 2024-04-17 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('companybranch', '0007_alter_branch_brcode'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='branch',
            unique_together={('company', 'brcode')},
        ),
    ]