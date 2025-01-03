# Generated by Django 5.1.4 on 2024-12-14 16:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product__id_product_about_product_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='product',
            name='index',
        ),
        migrations.AlterField(
            model_name='product',
            name='guid',
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]
