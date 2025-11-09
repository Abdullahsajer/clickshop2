# D:\pythonpro\clickshop2\catalog\views.py

from django.shortcuts import render
from .models import Product

def product_list_view(request):
    products = Product.objects.filter(is_active=True).select_related('category', 'brand')
    return render(request, 'catalog-templates/product_list.html', {'products': products})
