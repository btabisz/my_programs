from django.urls import path

from . import views
from .views import homepage, log, register, edit_profile, logout_view, EditProfileTemplateView, \
    add_product_view, cart_view, add_to_cart, my_search, delete_from_cart, add_product

urlpatterns = [
    path('', homepage, name='home'),
    path('login/', log, name='login'),
    path('register/', register, name='register'),
    path('edit/', edit_profile, name='edit'),
    path('edit_profil/', EditProfileTemplateView.as_view(), name='edit_profil'),
    path('logout/', logout_view, name='logout'),
    path('add_product_view/', add_product_view, name='add_product_view'),
    path('cart/', cart_view, name='cart'),
    path('delete_from_cart/', delete_from_cart, name='delete_from_cart'),
    path('add_to_cart/', add_to_cart, name='add_to_cart'),
    path('add_product/', add_product, name='add_product'),
    path('my_search/', my_search, name='my_search'),

]