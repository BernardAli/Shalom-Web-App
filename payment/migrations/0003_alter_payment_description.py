# Generated by Django 4.1.3 on 2023-06-30 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_alter_cash_category_alter_cashhistory_category'),
        ('payment', '0002_payment_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='description',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.cashflow'),
            preserve_default=False,
        ),
    ]
