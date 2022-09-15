# Generated by Django 3.2.12 on 2022-09-15 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0004_auto_20220916_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='visit.subcategory', verbose_name='Подкатегория'),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='visit.category', verbose_name='Категория'),
        ),
    ]
