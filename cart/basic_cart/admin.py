from django.contrib import admin
from .models import User, Product, Category, Cart
# Register your models here.

admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(Product)
