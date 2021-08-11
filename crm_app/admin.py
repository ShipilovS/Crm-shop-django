from django.contrib import admin
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'categories_foregin' ,'title', 'description']
    search_fields = ['title']

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'key_product', 'key_product_user', 'name', 'email']
    search_fields = ['name']

admin.site.register(Order, OrderAdmin)

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']

admin.site.register(Categories, CategoriesAdmin)
