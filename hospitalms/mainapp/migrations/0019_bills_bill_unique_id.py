# Generated by Django 4.1.4 on 2023-01-17 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0018_bills_payment_method_alter_bills_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bills',
            name='bill_unique_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
