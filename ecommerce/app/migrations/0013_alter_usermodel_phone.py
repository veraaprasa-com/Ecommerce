# Generated by Django 5.1.4 on 2024-12-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_usermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]