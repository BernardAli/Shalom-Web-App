# Generated by Django 4.1.3 on 2023-04-26 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_alter_testimony_testimony'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family',
            old_name='mission',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='family',
            name='vision',
        ),
    ]
