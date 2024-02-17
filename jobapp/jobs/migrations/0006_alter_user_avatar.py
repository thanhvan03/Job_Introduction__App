# Generated by Django 5.0.1 on 2024-02-08 13:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_comment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='avatar'),
        ),
    ]