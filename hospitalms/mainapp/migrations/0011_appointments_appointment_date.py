# Generated by Django 4.1.4 on 2023-01-11 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_appointments_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='appointment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]