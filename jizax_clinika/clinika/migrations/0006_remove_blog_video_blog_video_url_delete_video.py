# Generated by Django 4.2.7 on 2023-11-28 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinika', '0005_remove_blog_video_blog_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='video',
        ),
        migrations.AddField(
            model_name='blog',
            name='video_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]