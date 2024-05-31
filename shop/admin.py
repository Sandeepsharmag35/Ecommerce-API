from django.contrib import admin
from .models import Category, Product, Order, OrderItem
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id', 'name']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id', "name", "category", "stock", 'price']

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display=['id', "user", "created_at"]

admin.site.register(Order, OrderAdmin)

class OrderItemAdmin(admin.ModelAdmin):
    list_display=['id', "order"]

admin.site.register(OrderItem, OrderItemAdmin)
