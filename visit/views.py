from django.shortcuts import render
from .models import Product
from .models import Category
from .models import Subcategory

from django.shortcuts import render
from .models import SubCategory, Category
from django.http import HttpResponse
import json
def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'title'))
    return HttpResponse(json.dumps(result), content_type="application/json")


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
# Create your views here.
