# Generated by Django 5.1.4 on 2024-12-21 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('brand_description', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='colour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_description', models.TextField(max_length=1000)),
                ('model_height', models.CharField(max_length=100)),
                ('model_wearing', models.CharField(max_length=100)),
                ('care_instructions', models.CharField(max_length=100)),
                ('about', models.TextField(max_length=1000)),
                ('brand_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.brand')),
                ('product_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product_category')),
            ],
        ),
        migrations.CreateModel(
            name='product_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_price', models.IntegerField()),
                ('sale_price', models.IntegerField()),
                ('colour_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.colour')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
        ),
        migrations.CreateModel(
            name='product_image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_filename', models.TextField(max_length=100)),
                ('product_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product_item')),
            ],
        ),
        migrations.CreateModel(
            name='product_variation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty_in_stock', models.IntegerField()),
                ('product_item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product_item')),
                ('size_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.size_option')),
            ],
        ),
    ]
