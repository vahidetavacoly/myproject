# Generated by Django 5.1.2 on 2024-11-04 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_information_m_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information_m',
            name='codemeli',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='information_m',
            name='tell',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='information_m',
            name='zaman',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
