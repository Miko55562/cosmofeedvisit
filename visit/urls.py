from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('catalog', catalog),
    path('delivery', delivery),
]
