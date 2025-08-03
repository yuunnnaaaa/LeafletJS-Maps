from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import User, Product, Category
from .cart import CartHandler  # Update import
from django.contrib import messages
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

def pilihPaket(request):
    category = Category.objects.filter(status=0)
    context = {'category':category}
    return render(
        request,
        'pilihPaket.html', context
    )


def pilihProduk(request, slug):
    if(Category.objects.filter(slug=slug, status=0)):
        product = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'product' : product, 'category' : category}
        return render(request, "pilihProduk.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect('pilihPaket')


def detailProduk(request, cate_slug, prod_slug):
    if(Category.objects.filter(slug=cate_slug, status=0)):
        if(Product.objects.filter(slug=prod_slug, status=0)):
            products = Product.objects.filter(slug=prod_slug, status=0).first
            context = {'products':products}
        else:
            messages.warning(request, "No such product found")
            return redirect('pilihProduk')
    else:
        messages.warning(request, "No such category found")
        return redirect('pilihPaket')
    return render(request,"detailProduk.html", context)
