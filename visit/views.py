from django.shortcuts import render
from .models import Product
from .models import Category
from .models import Subcategory
from .models import ContactForm
from django.core.mail import send_mail

def index(request):
    if request.method == 'POST':
        print(request.POST)
        request_name = request.POST.get("name")
        request_mail = request.POST.get("mail")
        request_message = request.POST.get("message")
        ContactForm.objects.create(name=request_name,
                                    mail=request_mail,
                                    message=request_message)
    return render(request, template_name='visit/index.html')

def index_eng(request):
    if request.method == 'POST':
        request_name = request.POST.get("name")
        request_mail = request.POST.get("mail")
        request_message = request.POST.get("message")
        ContactForm.objects.create(name=request_name,
                                    mail=request_mail,
                                    message=request_message)
    return render(request, template_name='visit/index_eng.html')

def catalog(request):
    return render(request, template_name='visit/catalog.html')

def catalog_eng(request):
    return render(request, template_name='visit/catalog_eng.html')

def delivery(request):
    return render(request, template_name='visit/delivery.html')

def delivery_eng(request):
    return render(request, template_name='visit/delivery_eng.html')
