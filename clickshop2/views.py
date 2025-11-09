# D:\pythonpro\clickshop2\views.py
from django.shortcuts import render
from catalog.models import Product

def home_view(request):
    products = Product.objects.filter(is_active=True).order_by('-created_at')[:6]  # عرض آخر 6 منتجات فقط
    return render(request, 'home.html', {'products': products})
