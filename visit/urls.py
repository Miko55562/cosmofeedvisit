from django.urls import path
from django.views.generic.base import TemplateView

from .views import *

urlpatterns = [
    path('', index),
    path('catalog', catalog),
    path('delivery', delivery),
    path('index_eng', index_eng),
    path('delivery_eng', delivery_eng),
    path('catalog_eng', catalog_eng),
    path("robots.txt", robots),
]
