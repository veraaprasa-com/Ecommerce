# Generated by Django 5.1.4 on 2025-01-03 09:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.product_category'),
        ),
        migrations.AddField(
            model_name='product_item',
            name='size_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.size_category'),
        ),
    ]
