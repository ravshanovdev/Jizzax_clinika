# Generated by Django 4.2.5 on 2023-09-13 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinika', '0002_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]