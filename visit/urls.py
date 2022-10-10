from django.urls import path
from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('', index),
    path('catalog', catalog),
    path('delivery', delivery),
    path('category/<slug:category_slug>', catalog_subcat, name='category'),
    path("robots.txt", robots),
    path('catalog_subcat', catalog_subcat),
    path('product_big', product_big),
]
