# Generated by Django 5.1.4 on 2025-01-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_rename_colour_id_product_item_colour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_category',
            name='category_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_category/'),
        ),
    ]
