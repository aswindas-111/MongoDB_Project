# Generated by Django 3.2.24 on 2024-02-26 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_category_product'),
    ]

    operations = [
        migrations.DeleteModel(
            name='category',
        ),
        migrations.DeleteModel(
            name='product',
        ),
    ]
