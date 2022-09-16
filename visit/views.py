from django.shortcuts import render
from .models import Product
from .models import Category
from .models import Subcategory

def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    subcategory = Subcategory.objects.all()
    context = {
        'products': products,
        'categories': categories,
        'subcategory': subcategory,
    }
    return render(request, template_name='index.html', context=context)
