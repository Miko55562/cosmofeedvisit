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
    return render(request, template_name='visit/index.html')

def index_eng(request):
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
    return render(request, template_name='visit/index_eng.html')

def catalog(request):
    return render(request, template_name='visit/catalog.html')

def catalog_eng(request):
    return render(request, template_name='visit/catalog_eng.html')

def delivery(request):
    return render(request, template_name='visit/delivery.html')

def delivery_eng(request):
    return render(request, template_name='visit/delivery_eng.html')
