from django.urls import path
from .views import *

urlpatterns = [
    path('', listItem, name="content"),
    path('cart/', cart, name="cart"),
    path('checkout/', checkout, name="checkout"),
    path('content/', listItem, name='content'),
    path('register', register, name='register'),
    path('login', loginUser, name='login'),
    path('logout', logoutUser, name='logout'),
]