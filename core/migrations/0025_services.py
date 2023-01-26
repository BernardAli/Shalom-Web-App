# Generated by Django 4.1.3 on 2023-01-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0024_rename_subscribe_subscribers"),
    ]

    operations = [
        migrations.CreateModel(
            name="Services",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="default.jpg",
                        null=True,
                        upload_to="profile_pics",
                    ),
                ),
                ("times", models.TextField(blank=True, null=True)),
                ("days", models.TextField(blank=True, null=True)),
                ("descriptions", models.TextField(blank=True, null=True)),
            ],
        ),
    ]
