# Generated by Django 5.1.1 on 2024-11-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_information_m_end_time_information_m_start_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availability',
            name='consultant',
        ),
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='booking',
            name='consultant',
        ),
        migrations.RemoveField(
            model_name='sabtmoshaver',
            name='consultant',
        ),
        migrations.RemoveField(
            model_name='sabtmoshaver',
            name='user',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='consultant',
        ),
        migrations.RemoveField(
            model_name='users',
            name='moshaver',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user',
        ),
        migrations.AddField(
            model_name='appintment',
            name='codemeli',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='appintment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='appintment',
            name='namefull',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='appintment',
            name='tel',
            field=models.IntegerField(null=True),
        ),
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Availability',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='conulationcategory',
        ),
        migrations.DeleteModel(
            name='sabtmoshaver',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]
