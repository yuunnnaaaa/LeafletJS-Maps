from django.urls import path
from . import views

urlpatterns = [
    path('cart-details/',views.cart_summary, name='cart_summary'),
    path('add-teacher/',views.cart_add, name='cart_add'),
    path('deletee/',views.cart_delete_product, name='cart_delete_product'),
    # path('update/',views.cart_update, name='cart_update'),
]