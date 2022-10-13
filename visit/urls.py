from django.urls import path
from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('', index),
    path('catalog', catalog),
    path('delivery', delivery),
    path('category/<slug:category_slug>', catalog_category, name='catalog_category'),
    path('product/<int:product_pk>', product_big, name='product_big'),
    path('category/<slug:category_slug>/subcategory/<slug:subcategory_slug>', catalog_subcategory, name='catalog_subcategory'),
    path('robots.txt', robots),
]
