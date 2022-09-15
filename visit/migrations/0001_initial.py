# Generated by Django 3.2.12 on 2022-09-15 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Подкатегория')),
                ('сategory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visit.category')),
            ],
            options={
                'verbose_name': 'Подкатегория',
                'verbose_name_plural': 'Подкатегории',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Название')),
                ('product_code', models.CharField(max_length=150, null=True, verbose_name='Код Товара')),
                ('product_sku', models.CharField(max_length=150, null=True, verbose_name='Артикул товара')),
                ('manufacturer', models.CharField(max_length=150, null=True, verbose_name='Производитель')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('country_of_origin', models.CharField(max_length=150, null=True, verbose_name='Страна производства')),
                ('composition', models.CharField(max_length=150, null=True, verbose_name='Состав')),
                ('nutritional_value_of_100_grams', models.CharField(max_length=150, null=True, verbose_name='Пищевая ценность 100 грамм')),
                ('energy_value', models.CharField(max_length=150, null=True, verbose_name='Энергетическая ценность')),
                ('best_before_date', models.CharField(max_length=150, null=True, verbose_name='Срок годности')),
                ('type_of_packaging', models.CharField(max_length=150, null=True, verbose_name='Тип упаковки')),
                ('weight', models.CharField(max_length=150, null=True, verbose_name='Вес продукции')),
                ('price_is_for', models.CharField(max_length=150, null=True, verbose_name='Цена указана за')),
                ('availability', models.BooleanField(default=True, verbose_name='Наличие товара')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='visit.subcategory', verbose_name='Подкатегория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visit.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Фото продукта',
                'verbose_name_plural': 'Фото продуктов',
                'ordering': ['product'],
            },
        ),
    ]