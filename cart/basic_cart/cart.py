# cart.py
from .models import Cart, Product, User
import json
from decimal import Decimal
class CartHandler():  # Renaming from Cart to CartHandler
    def __init__(self, request):
        self.session = request.session
        self.request = request
        self.user = self.request.user

        if self.user.is_authenticated:
            self.cart_items = Cart.objects.filter(user=self.user)  # This refers to the Cart model
        else:
            self.cart_items = []

    def add_teacher(self, product):
        product_id = product.id
        cart_item, created = Cart.objects.get_or_create(user=self.user, product=product)
        if not created:
            cart_item.quantity = 1
            cart_item.save()
    
    def deleteproduct(self, product):
        Cart.objects.filter(user=self.user, product=product).delete()

    def cart_total(self):
        total = Decimal('0.00')
        for item in self.cart_items:
            if item.product and item.quantity:
                total += Decimal(item.product.sell_price) * Decimal(item.quantity)
        return total


    def __len__(self):
        return sum(item.quantity for item in self.cart_items)

    def get_prods(self):
        # Get IDs from cart_items
        product_ids = [item.product.id for item in self.cart_items if item.product]  # Collect product IDs
        # Use IDs to lookup products in the database model
        products = Product.objects.filter(id__in=product_ids)  # Query database for Products
        return products