# Generated by Django 4.1.3 on 2023-04-25 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_testimony'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimony',
            name='testimony',
            field=models.TextField(),
        ),
    ]
