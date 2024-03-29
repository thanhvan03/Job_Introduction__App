# Generated by Django 5.0.1 on 2024-02-04 08:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_alter_joblisting_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobapplication',
            name='introduce',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='resume',
            field=models.ImageField(null=True, upload_to='resume/%Y/%m'),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending', max_length=20),
        ),
    ]
