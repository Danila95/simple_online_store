# Generated by Django 2.1.3 on 2019-01-28 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_product_is_main'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
