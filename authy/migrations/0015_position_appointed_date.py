# Generated by Django 4.1.3 on 2023-04-27 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0014_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='appointed_date',
            field=models.DateField(default=datetime.datetime(2023, 4, 27, 15, 54, 43, 16292, tzinfo=datetime.timezone.utc)),
        ),
    ]