# Generated by Django 4.1.3 on 2023-01-25 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0023_subscribe"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Subscribe",
            new_name="Subscribers",
        ),
    ]