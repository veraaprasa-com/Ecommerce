# Generated by Django 5.1.4 on 2024-12-27 05:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_remove_addressmodel_user_alter_usermodels_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressmodel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.usermodels'),
        ),
        migrations.AlterField(
            model_name='usermodels',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]