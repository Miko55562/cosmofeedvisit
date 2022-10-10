from django.contrib import admin
from .models import Product, Category, Subcategory, Photo, ContactForm, Malling, AllowedCombination
from .forms import ProductForm

class ProductAdmin(admin.ModelAdmin):
    form = ProductForm
    list_display = ('id', 'name', 'product_code', 'availability', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'product_code', 'product_sku')
    list_filter = ('is_published',)
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


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')
    list_display_links = ('id', 'product')
    search_fields = ('product',)


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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Malling, MallingAdmin)
admin.site.register(AllowedCombination, AllowedCombinationAdmin)

admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'
