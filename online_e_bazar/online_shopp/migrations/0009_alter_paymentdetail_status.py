# Generated by Django 4.2.4 on 2023-08-22 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shopp', '0008_alter_paymentdetail_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentdetail',
            name='status',
            field=models.CharField(choices=[('1', 'Paid'), ('2', 'No Paid')], max_length=255),
        ),
    ]
