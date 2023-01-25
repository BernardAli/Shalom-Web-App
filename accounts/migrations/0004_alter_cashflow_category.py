# Generated by Django 4.1.3 on 2023-01-25 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_rename_cashflows_cashflow"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cashflow",
            name="category",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="accounts.category",
            ),
        ),
    ]