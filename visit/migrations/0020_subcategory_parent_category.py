# Generated by Django 3.2.12 on 2022-10-09 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visit', '0019_category_parent_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visit.category'),
        ),
    ]
