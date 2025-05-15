from django.urls import path
from .views import (
    product_list, add_to_cart, remove_from_cart, cart_view,
    checkout, checkout_success, order_history,
    signup, user_login, user_logout
)

urlpatterns = [
    # ✅ Product & Cart Management
    path('', product_list, name='product_list'),
    path('cart/', cart_view, name='cart_view'),
    path('checkout/', checkout, name='checkout'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),

    # ✅ Checkout & Order History
    path('checkout-success/', checkout_success, name='checkout_success'),
    path('order-history/', order_history, name='order_history'),

    # ✅ User Authentication
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]