# Generated by Django 4.1.4 on 2023-01-11 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_appointments_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='appointment_time',
            field=models.DateTimeField(),
        ),
    ]