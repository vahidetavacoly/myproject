# Generated by Django 5.1.1 on 2024-12-30 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_alter_information_m_codemeli_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information_m',
            name='codemeli',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.AlterField(
            model_name='information_m',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
