# urls.py
from django.urls import path
from .views import shop_view, cart_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('shop/', shop_view, name='shop'),
    path('cart/', cart_view, name='cart'),
]
