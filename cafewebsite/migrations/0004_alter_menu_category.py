# Generated by Django 5.0.2 on 2024-03-29 22:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafewebsite', '0003_remove_menu_image1_remove_menu_image2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafewebsite.category'),
        ),
    ]
