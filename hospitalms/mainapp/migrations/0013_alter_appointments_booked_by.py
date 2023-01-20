# Generated by Django 4.1.4 on 2023-01-11 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_alter_appointments_appointment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointments',
            name='booked_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
