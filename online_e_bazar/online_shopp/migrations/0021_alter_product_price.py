# Generated by Django 4.2.4 on 2023-08-31 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shopp', '0020_alter_paymentdetail_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(max_length=100000000000),
        ),
    ]