# Generated by Django 4.1.3 on 2023-04-27 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_cash_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='cash',
            name='account_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
