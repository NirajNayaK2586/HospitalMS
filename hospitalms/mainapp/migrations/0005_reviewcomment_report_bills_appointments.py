# Generated by Django 4.1.4 on 2022-12-24 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_receptionist_patient_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateTimeField(auto_now=True)),
                ('review_rating', models.IntegerField()),
                ('review_comment', models.TextField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report_title', models.CharField(max_length=50)),
                ('report', models.FileField(upload_to='report_file')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_title', models.CharField(max_length=50)),
                ('issue_date', models.DateTimeField(auto_now=True)),
                ('bill', models.FileField(upload_to='bills_file')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_at', models.DateTimeField(auto_now=True)),
                ('appointment_time', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('booked_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.patient')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.doctor')),
            ],
        ),
    ]
