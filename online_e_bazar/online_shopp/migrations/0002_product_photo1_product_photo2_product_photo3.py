# Generated by Django 4.2.1 on 2023-06-02 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shopp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo1',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo2',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]