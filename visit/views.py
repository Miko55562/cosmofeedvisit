from django.shortcuts import render
from .models import Product
from .models import Category
from .models import Subcategory

def index(request):
    return render(request, template_name='visit/index.html')

def index_eng(request):
    return render(request, template_name='visit/index_eng.html')

def catalog(request):
    return render(request, template_name='visit/catalog.html')

def catalog_eng(request):
    return render(request, template_name='visit/catalog_eng.html')

def delivery(request):
    return render(request, template_name='visit/delivery.html')

def delivery_eng(request):
    return render(request, template_name='visit/delivery_eng.html')
