# Generated by Django 4.1.3 on 2023-04-27 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_cash_receipt_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash',
            name='account_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
