# Generated by Django 5.1.3 on 2024-11-27 15:12

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/your_cloud_name/image/upload/v1234567890/default_profile_rnezic.png', max_length=255, verbose_name='image'),
        ),
    ]