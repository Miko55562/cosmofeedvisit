from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Subcategory(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Подкатегория')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'
        ordering = ['title']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')

    product_code = models.CharField(max_length=150, verbose_name='Код Товара 1', null=True)
    weight = models.CharField(max_length=150, verbose_name='Вес продукции 1', null=True)

    product_code_2 = models.CharField(max_length=150, verbose_name='Код Товара 2', null=True)
    weight_2 = models.CharField(max_length=150, verbose_name='Вес продукции 2', null=True)

    product_code_3 = models.CharField(max_length=150, verbose_name='Код Товара 3', null=True)
    weight_3 = models.CharField(max_length=150, verbose_name='Вес продукции 3', null=True)

    product_code_4 = models.CharField(max_length=150, verbose_name='Код Товара 4', null=True)
    weight_4 = models.CharField(max_length=150, verbose_name='Вес продукции 4', null=True)

    product_code_5 = models.CharField(max_length=150, verbose_name='Код Товара 5', null=True)
    weight_5 = models.CharField(max_length=150, verbose_name='Вес продукции 5', null=True)

    product_code_6 = models.CharField(max_length=150, verbose_name='Код Товара 6', null=True)
    weight_6 = models.CharField(max_length=150, verbose_name='Вес продукции 6', null=True)

    product_sku = models.CharField(max_length=150, verbose_name='Артикул товара', null=True)

    manufacturer = models.CharField(max_length=150, verbose_name='Производитель', null=True)

    description = models.TextField(blank=True, verbose_name='Описание', null=True)

    # Характеристики
    country_of_origin = models.CharField(max_length=150, verbose_name='Страна производства', null=True)
    composition = models.CharField(max_length=150, verbose_name='Состав', null=True)
    nutritional_value_of_100_grams = models.CharField(max_length=150, verbose_name='Пищевая ценность 100 грамм', null=True)
    energy_value = models.CharField(max_length=150, verbose_name='Энергетическая ценность', null=True)
    best_before_date = models.CharField(max_length=150, verbose_name='Срок годности', null=True)
    type_of_packaging = models.CharField(max_length=150, verbose_name='Тип упаковки', null=True)
    price_is_for = models.CharField(max_length=150, verbose_name='Цена указана за', null=True)

    availability = models.BooleanField(default=True, verbose_name='Наличие товара')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    subcategory =  models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']


class AllowedCombination(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    subcategory =  models.ForeignKey(Subcategory, on_delete=models.CASCADE, verbose_name='Подкатегория')

    def __str__(self):
        return f'{self.category} {self.subcategory}'


    class Meta:
        verbose_name = 'Комбинацию'
        verbose_name_plural = 'Комбинации'


class Photo(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Продукт')
    image = models.ImageField(blank = True)


    class Meta:
        verbose_name = 'Фото продукта'
        verbose_name_plural = 'Фото продуктов'
        ordering = ['product']


class ContactForm(models.Model):
    name = models.CharField(max_length=150, verbose_name='Имя')
    mail = models.EmailField(verbose_name='Электронная почта')
    sity = models.CharField(max_length=150, verbose_name='Город')
    message = models.TextField(max_length=150, verbose_name='Сообщение')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
        ordering = ['-created_at']


class Malling(models.Model):
    mail = models.EmailField(verbose_name='Электронная почта', unique=True)

    def __str__(self):
        return self.mail

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['id']
