# Generated by Django 4.1.3 on 2023-02-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authy", "0009_alter_profile_family"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="blood_group",
            field=models.CharField(
                blank=True,
                choices=[
                    ("O-", "O-"),
                    ("O+", "O+"),
                    ("A-", "A-"),
                    ("A+", "A+"),
                    ("AB-", "AB-"),
                    ("AB+", "AB+"),
                    ("B-", "B"),
                    ("B+", "B+"),
                ],
                max_length=50,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="gender",
            field=models.CharField(
                blank=True,
                choices=[("Male", "Male"), ("Female", "Female")],
                max_length=50,
                null=True,
            ),
        ),
    ]
