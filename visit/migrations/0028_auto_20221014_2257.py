# Generated by Django 3.2.12 on 2022-10-14 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0027_auto_20221012_2333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.DeleteModel(
            name='AllowedCombination',
        ),
        migrations.DeleteModel(
            name='Subcategory',
        ),
    ]