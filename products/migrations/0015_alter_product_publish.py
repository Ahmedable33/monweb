# Generated by Django 4.2.7 on 2024-03-20 18:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_product_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publish',
            field=models.DateField(default=datetime.datetime(2024, 3, 20, 18, 11, 24, 791158)),
        ),
    ]
