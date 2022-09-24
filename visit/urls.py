from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('catalog', catalog),
    path('delivery', delivery),
    path('index_eng', index_eng),
    path('delivery_eng', delivery_eng),
]
