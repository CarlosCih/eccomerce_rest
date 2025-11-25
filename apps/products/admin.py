from django.contrib import admin
from .models import *


class MeseasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'state', 'created_date')
    search_fields = ('description',)
    list_filter = ('state',)

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'state', 'created_date')
    search_fields = ('description',)
    list_filter = ('state',)
    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'measure_unit', 'category_product', 'state', 'created_date')
    search_fields = ('name', 'measure_unit__description', 'category_product__description',)
    list_filter = ('state', 'measure_unit', 'category_product',)
       
# Register your models here.
admin.site.register(MeasureUnit, MeseasureUnitAdmin)
admin.site.register(CategoryProduct, CategoryProductAdmin)
admin.site.register(Indicator)
admin.site.register(Product, ProductAdmin)