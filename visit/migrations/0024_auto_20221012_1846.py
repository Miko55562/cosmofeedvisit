# Generated by Django 3.2.12 on 2022-10-12 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0023_rename_parent_category_subcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_1',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Главное фото продукта'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Фото продукта'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Фото продукта'),
        ),
    ]
