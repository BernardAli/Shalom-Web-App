# Generated by Django 4.1.3 on 2023-01-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_auxiliariesfaq"),
    ]

    operations = [
        migrations.RenameField(
            model_name="auxiliaries",
            old_name="image",
            new_name="deacon",
        ),
        migrations.AddField(
            model_name="auxiliaries",
            name="group_img",
            field=models.ImageField(default="group.png", upload_to="auxiliaries"),
        ),
    ]
