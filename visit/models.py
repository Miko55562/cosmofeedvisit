from django.db import models
from smart_selects.db_fields import ChainedForeignKey
from pytils import translit
from adminsortable.models import SortableMixin


class Category(SortableMixin):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['order']
    order = models.PositiveIntegerField(default=0, editable=False)
    def __str__(self):
        return self.title

class Product(models.Model):

    def get_image_path(self, filename):
           path = ''.join(["media/",translit.slugify(filename)])
           return path

    name = models.CharField(max_length=150, verbose_name='Название')

    prise = models.CharField(max_length=150, verbose_name='Цена продукции 1', null=True, blank=True)
    weight = models.CharField(max_length=150, verbose_name='Вес продукции 1', null=True, blank=True)
    type_of_packaging = models.CharField(max_length=150, verbose_name='Тип упаковки 1', null=True, blank=True)

    prise_2 = models.CharField(max_length=150, verbose_name='Цена продукции 2', null=True, blank=True)
    weight_2 = models.CharField(max_length=150, verbose_name='Вес продукции 2', null=True, blank=True)
    type_of_packaging_2 = models.CharField(max_length=150, verbose_name='Тип упаковки 2', null=True, blank=True)

    prise_3 = models.CharField(max_length=150, verbose_name='Цена продукции 3', null=True, blank=True)
    weight_3 = models.CharField(max_length=150, verbose_name='Вес продукции 3', null=True, blank=True)
    type_of_packaging_3 = models.CharField(max_length=150, verbose_name='Тип упаковки 3', null=True, blank=True)

    prise_4 = models.CharField(max_length=150, verbose_name='Цена продукции 4', null=True, blank=True)
    weight_4 = models.CharField(max_length=150, verbose_name='Вес продукции 4', null=True, blank=True)
    type_of_packaging_4 = models.CharField(max_length=150, verbose_name='Тип упаковки 4', null=True, blank=True)

    prise_5 = models.CharField(max_length=150, verbose_name='Цена продукции 5', null=True, blank=True)
    weight_5 = models.CharField(max_length=150, verbose_name='Вес продукции 5', null=True, blank=True)
    type_of_packaging_5 = models.CharField(max_length=150, verbose_name='Тип упаковки 5', null=True, blank=True)

    prise_6 = models.CharField(max_length=150, verbose_name='Цена продукции 6', null=True, blank=True)
    weight_6 = models.CharField(max_length=150, verbose_name='Вес продукции 6', null=True, blank=True)
    type_of_packaging_6 = models.CharField(max_length=150, verbose_name='Тип упаковки 6', null=True, blank=True)

    product_sku = models.CharField(max_length=150, verbose_name='Артикул товара', null=True, blank=True)

    manufacturer = models.CharField(max_length=150, verbose_name='Производитель', null=True, blank=True)

    description = models.TextField(blank=True, verbose_name='Описание', null=True)

    image_1 = models.ImageField(blank = True, verbose_name='Главное фото продукта', upload_to=get_image_path)
    image_2 = models.ImageField(blank = True, verbose_name='Фото продукта', upload_to=get_image_path)
    image_3 = models.ImageField(blank = True, verbose_name='Фото продукта', upload_to=get_image_path)
    image_4 = models.ImageField(blank = True, verbose_name='Фото продукта', upload_to=get_image_path)
    image_5 = models.ImageField(blank = True, verbose_name='Фото продукта', upload_to=get_image_path)
    image_6 = models.ImageField(blank = True, verbose_name='Фото продукта', upload_to=get_image_path)

    # Характеристики
    country_of_origin = models.CharField(max_length=150, verbose_name='Страна производства', null=True, blank=True)
    composition = models.TextField(max_length=355, verbose_name='Состав', null=True, blank=True)
    nutritional_value_of_100_grams = models.CharField(max_length=150, verbose_name='Пищевая ценность 100 грамм', null=True, blank=True)
    energy_value = models.CharField(max_length=150, verbose_name='Энергетическая ценность', null=True, blank=True)
    best_before_date = models.CharField(max_length=150, verbose_name='Срок годности', null=True, blank=True)


    availability = models.BooleanField(default=True, verbose_name='Наличие товара')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name']


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


class Partner(models.Model):
    def get_image_path(self, filename):
           path = ''.join(["media/",translit.slugify(filename)])
           return path
    image = models.ImageField(blank = True, verbose_name='Логотип', upload_to=get_image_path)

    class Meta:
        verbose_name = 'Партнёра'
        verbose_name_plural = 'Партнеры'
        ordering = ['id']


class CaruselProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Карусель Продуктов'
        ordering = ['id']

class CatalogFile(models.Model):
    file = models.FileField(upload_to='CatalogFile', verbose_name='Файл')

    class Meta:
        verbose_name = 'Прайслист'
        verbose_name_plural = 'Прайслист'
        ordering = ['id']
