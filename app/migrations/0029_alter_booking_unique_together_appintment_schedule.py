# Generated by Django 5.1.1 on 2024-11-25 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_availability_booking'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('consultant', 'date1', 'time')},
        ),
        migrations.CreateModel(
            name='Appintment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='')),
                ('time', models.TimeField(verbose_name='')),
                ('client_name', models.CharField(max_length=100, verbose_name='')),
                ('is_confirmed', models.BooleanField(default=False)),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.information_m', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('start_time', models.TimeField(verbose_name='')),
                ('end_time', models.TimeField(verbose_name='')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.information_m', verbose_name='')),
            ],
        ),
    ]
