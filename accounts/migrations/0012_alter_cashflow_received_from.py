# Generated by Django 4.1.3 on 2023-01-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0011_alter_cash_issue_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cashflow",
            name="received_from",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
