from django.contrib import admin
from .models import Product, Category, Subcategory, Photo, ContactForm, Malling


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product_code', 'availability', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'product_code', 'product_sku')
    list_filter = ('is_published',)
    list_editable = ('is_published', 'availability')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'parent', 'title')
    list_display_links = ('id', 'title', )
    search_fields = ('title', )


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')
    list_display_links = ('id', 'product')
    search_fields = ('product',)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', 'mail')


class MallingAdmin(admin.ModelAdmin):
    list_display = ('id', 'mail')
    list_display_links = ('id', 'mail')
    search_fields = ('id', 'mail')


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(Malling, MallingAdmin)


admin.site.site_title = 'Админ-панель'
admin.site.site_header = 'Админ-панель'
