# Generated by Django 4.1.3 on 2023-01-30 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0029_alter_family_deacon_alter_family_group_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auxiliaries",
            name="deacon",
            field=models.ImageField(
                blank=True, default="group.png", null=True, upload_to="auxiliaries"
            ),
        ),
        migrations.AlterField(
            model_name="auxiliaries",
            name="group_img",
            field=models.ImageField(
                blank=True, default="group.png", null=True, upload_to="auxiliaries"
            ),
        ),
    ]
