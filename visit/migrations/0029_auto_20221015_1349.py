# Generated by Django 3.2.12 on 2022-10-15 10:49

from django.db import migrations, models
import visit.models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0028_auto_20221014_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_is_for',
        ),
        migrations.AlterField(
            model_name='partner',
            name='image',
            field=models.ImageField(blank=True, upload_to=visit.models.Partner.get_image_path, verbose_name='Логотип'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_1',
            field=models.ImageField(blank=True, upload_to=visit.models.Product.get_image_path, verbose_name='Главное фото продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, upload_to=visit.models.Product.get_image_path, verbose_name='Фото продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, upload_to=visit.models.Product.get_image_path, verbose_name='Фото продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, upload_to=visit.models.Product.get_image_path, verbose_name='Фото продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_5',
            field=models.ImageField(blank=True, upload_to=visit.models.Product.get_image_path, verbose_name='Фото продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_6',
            field=models.ImageField(blank=True, upload_to=visit.models.Product.get_image_path, verbose_name='Фото продукта'),
        ),
    ]