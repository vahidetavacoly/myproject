# Generated by Django 5.1.1 on 2024-12-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_remove_information_m_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tamas',
            name='ip',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
