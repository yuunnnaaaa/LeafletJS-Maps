from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import User, Product
from .cart import CartHandler  # Update import

# Create your views here.

def cart_summary(request):
    cart = CartHandler(request)
    cart_products = cart.get_prods()
    totals = cart.cart_total()
    return render(request, "cart.html", {'cart_products': cart_products, 'totals': totals})

def cart_add(request):
    cart = CartHandler(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add_teacher(product=product)
        cart_quantity = len(cart)
        return JsonResponse({'qty': cart_quantity})
    
def cart_delete_product(request):
    cart = CartHandler(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.deleteproduct(product=product_id)
        return JsonResponse({'product': product_id})