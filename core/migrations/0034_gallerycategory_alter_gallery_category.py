# Generated by Django 4.1.3 on 2023-02-04 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0033_gallery"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalleryCategory",
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
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Services", "Service"),
                            ("Youth", "Youth"),
                            ("Projects", "Projects"),
                            ("Others", "Others"),
                        ],
                        max_length=50,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="gallery",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.gallerycategory"
            ),
        ),
    ]
