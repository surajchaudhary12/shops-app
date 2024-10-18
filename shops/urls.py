# shops/urls.py

from django.urls import path
from .views import ShopRegistrationView, UserSearchView

urlpatterns = [
    path('register/', ShopRegistrationView.as_view(), name='shop-register'),
    path('search/', UserSearchView.as_view(), name='shop-search'),
]