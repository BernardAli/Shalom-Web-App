# Generated by Django 4.1.3 on 2023-01-13 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authy", "0002_rename_club_profile_family"),
        ("core", "0003_club"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Club",
            new_name="Family",
        ),
    ]