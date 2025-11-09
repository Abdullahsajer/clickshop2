# D:\pythonpro\clickshop2\catalog\urls.py

from django.urls import path
from .views import product_list_view

app_name = 'catalog'

urlpatterns = [
    path('products/', product_list_view, name='product_list'),
]
