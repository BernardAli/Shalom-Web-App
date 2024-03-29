# Generated by Django 4.1.3 on 2023-04-27 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0013_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=50)),
                ('salary', models.IntegerField(default=0)),
                ('appointment_letter', models.FileField(upload_to='')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authy.employees')),
            ],
        ),
    ]
