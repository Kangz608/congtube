# Generated by Django 2.2.5 on 2019-11-01 02:53

import banners.models.banner
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='url',
            field=models.URLField(default=' ', verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to=banners.models._banner_image_upload_to, verbose_name='이미지'),
        ),
    ]
