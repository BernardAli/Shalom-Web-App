# Generated by Django 4.1.3 on 2023-01-23 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_rename_text_faq_answer_rename_title_faq_question"),
    ]

    operations = [
        migrations.CreateModel(
            name="AuxiliariesFAQ",
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
                ("question", models.CharField(max_length=250)),
                ("answer", models.TextField()),
                (
                    "auxiliary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="auxiliary_faqs",
                        to="core.auxiliaries",
                    ),
                ),
            ],
        ),
    ]
