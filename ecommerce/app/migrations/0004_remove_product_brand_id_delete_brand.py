# Generated by Django 5.1.4 on 2024-12-22 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_product_category_category_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand_id',
        ),
        migrations.DeleteModel(
            name='brand',
        ),
    ]