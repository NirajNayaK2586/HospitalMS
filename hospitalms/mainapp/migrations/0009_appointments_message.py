# Generated by Django 4.1.4 on 2023-01-10 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_doctor_doctor_image_doctor_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointments',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
