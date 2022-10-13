from django.urls import path
from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('', index),
    path('catalog', catalog),
    path('delivery', delivery),
    path('partners', partners),
    path('category/<slug:category_slug>', catalog_category, name='catalog_category'),
    path('category/<slug:category_slug>/subcategory/<slug:subcategory_slug>', catalog_subcategory, name='catalog_subcategory'),
    path('product/<int:product_pk>', product_big, name='product_big'),
    path('robots.txt', robots),
]
