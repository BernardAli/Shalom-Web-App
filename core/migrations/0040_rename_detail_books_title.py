# Generated by Django 4.1.3 on 2023-04-27 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0039_books_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='detail',
            new_name='title',
        ),
    ]
