# Generated by Django 5.1.1 on 2024-11-26 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_booking_unique_together_appintment_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='information_m',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='information_m',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
