# Generated by Django 4.1.4 on 2023-01-17 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0020_alter_bills_bill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bills',
            old_name='bill_unique_id',
            new_name='remarks',
        ),
    ]
