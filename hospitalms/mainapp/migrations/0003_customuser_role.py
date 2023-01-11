# Generated by Django 4.1.4 on 2022-12-22 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_customuser_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to='mainapp.role'),
        ),
    ]
