from django.contrib import admin
from .models import Product, Cart, Customer, Order

# Register your models here.

admin.site.register(Order)
admin.site.register(Cart)
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('username', 'email_address', 'phone_number')
    search_fields = ['username']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'description', 'image')
    search_fields = ['name']

