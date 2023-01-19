# Generated by Django 4.1.3 on 2023-01-13 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0003_club"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        default="default.jpg",
                        null=True,
                        upload_to="profile_pics",
                    ),
                ),
                ("created", models.DateField(auto_now_add=True)),
                (
                    "user_type",
                    models.CharField(
                        choices=[("User", "User"), ("Member", "Member")],
                        default="User",
                        max_length=20,
                    ),
                ),
                ("phone", models.CharField(max_length=20)),
                ("next_of_kin", models.CharField(max_length=100)),
                (
                    "next_of_kin_contact",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "club",
                    models.ForeignKey(
                        blank=True,
                        default=1,
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="core.club",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="profile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]