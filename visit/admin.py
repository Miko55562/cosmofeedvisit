from django.contrib import admin
from .models import Product, Category, Subcategory, Photo
from .forms import ProductForm
import logging
# какая то штука
class ProductAdmin(admin.ModelAdmin):
    logging.warning(ProductForm)
    '''
    def render_change_form(self, request, context, *args, **kwargs):
        context['adminform'].form.fields['subcategory'].queryset = Subcategory.objects.filter(
        parent=1)
        return super(ProductAdmin, self).render_change_form(request, context, *args, **kwargs)
    '''
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

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Photo, PhotoAdmin)
