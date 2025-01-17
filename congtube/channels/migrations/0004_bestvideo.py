# Generated by Django 2.2.5 on 2019-12-10 11:15

import channels.models.bestvideo
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0003_auto_20191210_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to=channels.models.bestvideo._channel_video_upload_to, verbose_name='동영상')),
                ('is_display', models.BooleanField(blank=True, default=True, verbose_name='표시')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channels.Channel')),
            ],
            options={
                'verbose_name': '베스트 비디오',
                'verbose_name_plural': '베스트 비디오',
            },
        ),
    ]
