# Generated by Django 3.2.12 on 2022-10-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0024_auto_20221012_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prise',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Цена продукции 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='prise_2',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Цена продукции 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='prise_3',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Цена продукции 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='prise_4',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Цена продукции 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='prise_5',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Цена продукции 1'),
        ),
        migrations.AddField(
            model_name='product',
            name='prise_6',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Цена продукции 1'),
        ),
    ]