from django.shortcuts import render
from .models import Product
from .models import Category
from .models import Subcategory
from .models import ContactForm
from .models import Malling
from .models import CaruselProduct
from .models import CatalogFile

from django.core.mail import send_mail
import os
from django.conf import settings
from django.http import HttpResponse, Http404

def robots(request):
    return render(request, template_name='visit/robots.txt', content_type="text/plain")

def download(request):
    print(request)
    path = CatalogFile.objects.get(id=1)
    file_path = os.path.join(settings.MEDIA_ROOT, str(path.file))
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

def index(request):
    if request.method == 'GET' and request.GET.get('download'):
        return download(request)

    if request.method == 'POST' and request.POST.get('ContactForm'):
        request_name = request.POST.get("name")
        request_mail = request.POST.get("mail")
        request_message = request.POST.get("message")
        request_sity = request.POST.get("sity")
        ContactForm.objects.create(name=request_name,
                                    mail=request_mail,
                                    sity=request_sity,
                                    message=request_message)
    elif request.method == 'POST' and request.POST.get('Mailing'):
        request_name = request.POST.get("mail_mailler")
        Malling.objects.get_or_create(mail=request_name)

    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    carusel_product = CaruselProduct.objects.order_by('product')
    context = {
    'categories': categories,
    'carusel_product': carusel_product,
    }
    return render(request, template_name='visit/index.html', context=context)

def category(request, category_id):
    if request.method == 'GET' and request.GET.get('download'):
        return download(request)

    subcategory = Subcategory.objects.filter(category_id = category_id)
    context = {
    'subcategory': subcategory,
    }
    if len(subcategory) == 0:
        raise Http404()

    return render(request, template_name='visit/catalog.html', context=context)

def catalog_category(request, category_slug):
    if request.method == 'GET' and request.GET.get('download'):
        return download(request)

    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category_id = category.id)
    subcategories = Subcategory.objects.filter(category_id=category.id)
    context = {
    'subcategories': subcategories,
    'categories': categories,
    'products': products,
    'category_slug': category_slug,
    }
    return render(request, template_name='visit/catalog_subcat.html', context=context)

def catalog_subcategory(request, category_slug, subcategory_slug):
    if request.method == 'GET' and request.GET.get('download'):
        return download(request)

    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    subcategory = Subcategory.objects.get(slug=subcategory_slug)
    subcategories = Subcategory.objects.filter(category_id=category.id)
    print(subcategories)
    products = Product.objects.filter(category_id = category.id,
                                      subcategory_id = subcategory.id)
    context = {
    'subcategories': subcategories,
    'categories': categories,
    'products': products,
    'category_slug': category_slug,
    }
    return render(request, template_name='visit/catalog_subcat.html', context=context)

def catalog(request):
    if request.method == 'GET' and request.GET.get('download'):
        return download(request)

    categories = Category.objects.all()
    context = {
    'categories': categories,
    }
    return render(request, template_name='visit/catalog.html', context=context)

def delivery(request):
    if request.method == 'GET' and request.GET.get('download'):
        return download(request)

    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {
    'categories': categories,
    }
    return render(request, template_name='visit/delivery.html', context=context)

def product_big(request, product_pk):
    if request.method == 'GET' and request.GET.get('download'):
        return download(request)

    product = Product.objects.get(pk=product_pk)
    context = {
    'product':product
    }
    return render(request, template_name='visit/product_big.html', context=context)
