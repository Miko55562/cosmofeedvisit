from django.contrib import admin
from .models import Product
from .models import Category
from .models import Subcategory
from .models import ContactForm
from .models import Malling
from .models import AllowedCombination
from .models import Partner
from .models import CaruselProduct
from .models import CatalogFile
from .forms import ProductForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('id', 'name', 'product_code', 'availability', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'product_code', 'product_sku')
    list_filter = ('is_published', 'category', 'subcategory')
    list_editable = ('is_published', 'availability')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title', )
    search_fields = ('title', )
    prepopulated_fields = {"slug": ("title",)}


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'sity', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'mail')


class MallingAdmin(admin.ModelAdmin):
    list_display = ('id', 'mail')
    list_display_links = ('id', 'mail')
    search_fields = ('id', 'mail')


class AllowedCombinationAdmin(admin.ModelAdmin):
    list_display = ['category', 'subcategory']


class PartnerAdmin(admin.ModelAdmin):
    list_display = ['id']


class CaruselProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product']


class CatalogFileAdmin(admin.ModelAdmin):
    list_display = ['id']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Malling, MallingAdmin)
admin.site.register(AllowedCombination, AllowedCombinationAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(CaruselProduct, CaruselProductAdmin)
admin.site.register(CatalogFile, CatalogFileAdmin)

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'
