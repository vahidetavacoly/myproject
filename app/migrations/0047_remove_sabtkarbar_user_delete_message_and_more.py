# Generated by Django 5.1.2 on 2025-01-02 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_information_m_rozonline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sabtkarbar',
            name='user',
        ),
        migrations.DeleteModel(
            name='message',
        ),
        migrations.DeleteModel(
            name='sabtkarbar',
        ),
    ]
