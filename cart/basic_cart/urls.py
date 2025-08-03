from django.urls import path
from . import views

urlpatterns = [
    path('cart-details/',views.cart_summary, name='cart_summary'),
    path('add-teacher/',views.cart_add, name='cart_add'),
    path('deletee/',views.cart_delete_product, name='cart_delete_product'),
    path('pilihan-paket', views.pilihPaket, name='pilihPaket'),
    path('pilihan-paket/<str:slug>', views.pilihProduk, name='pilihProduk'),
    path('pilihan-paket/<str:cate_slug>/<str:prod_slug>', views.detailProduk, name='detailProduk'),
]