from django.contrib import admin
from django.urls import path
from .views import home, search, get_info, get_ukraine_map, cryptocurrencies, crypto_usage, home_page_return


urlpatterns = [
    path('', home, name='home'),
    path(r'^/search$', search, name='search'),
    path('/get_info', get_info, name='get_info'),
    path('/map', get_ukraine_map, name='get_map'),
    path('/cryptocurrencies', cryptocurrencies, name="cryptocurrencies"),
    path('/crypto_usage', crypto_usage, name="crypto_usage"),
    path(r'^.+$', home_page_return, name='home_page_return'),
]