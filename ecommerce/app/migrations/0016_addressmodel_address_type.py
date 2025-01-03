# Generated by Django 5.1.4 on 2024-12-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_rename_user_adrs_addressmodel_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressmodel',
            name='address_type',
            field=models.CharField(blank=True, choices=[('B', 'Billing'), ('S', 'Shipping')], max_length=1, null=True),
        ),
    ]
