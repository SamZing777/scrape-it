# Generated by Django 4.0.4 on 2022-05-08 14:33

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=cloudinary.models.CloudinaryField(default='https://i.stack.imgur.com/0Jl54.png', max_length=255, verbose_name='image'),
        ),
    ]
