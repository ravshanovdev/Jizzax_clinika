# Generated by Django 4.2.4 on 2023-08-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shopp', '0011_remove_orderitems_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
