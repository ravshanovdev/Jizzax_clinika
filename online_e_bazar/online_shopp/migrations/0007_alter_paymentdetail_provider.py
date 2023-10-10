# Generated by Django 4.2.4 on 2023-08-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shopp', '0006_alter_paymentdetail_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetail',
            name='provider',
            field=models.CharField(choices=[('humo', 'HUMO'), ('uzcard', 'UzCard'), ('visa', 'VISA'), ('mastercard', 'MasterCard')], default='Choose Your Payment Provider', max_length=255),
        ),
    ]
