# Generated by Django 4.2.4 on 2023-08-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shopp', '0013_cartitem_product_id_cartitem_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='total_items',
            field=models.IntegerField(default=0),
        ),
    ]