from django.shortcuts import render
from .models import Product
from .models import Category
from .models import Subcategory
from .models import ContactForm
from .models import Malling
from django.core.mail import send_mail


def robots(request):
    return render(request, template_name='visit/robots.txt', content_type="text/plain")

def index(request):
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
    context = {
    'categories': categories,
    }
    print(subcategories)
    return render(request, template_name='visit/index.html', context=context)

def category(request, category_id):
    subcategory = Subcategory.objects.filter(category_id = category_id)
    context = {
    'subcategory': subcategory,
    }
    if len(subcategory) == 0:
        raise Http404()

    return render(request, template_name='visit/catalog.html', context=context)

def catalog_subcat(request, category_slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=category_slug)
    products = Product.objects.filter(category_id = category.id)
    context = {
    'categories': categories,
    'products': products,
    }
    return render(request, template_name='visit/catalog_subcat.html', context=context)

def catalog(request):
    categories = Category.objects.all()
    context = {
    'categories': categories,
    }
    return render(request, template_name='visit/catalog.html', context=context)

def delivery(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {
    'categories': categories,
    }
    return render(request, template_name='visit/delivery.html', context=context)

def product_big(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    context = {
    'product':product
    }
    return render(request, template_name='visit/product_big.html', context=context)
