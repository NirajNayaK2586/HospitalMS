# Generated by Django 4.1.4 on 2023-01-17 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_bills_bill_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='bill',
            field=models.FileField(blank=True, null=True, upload_to='bills_file'),
        ),
    ]