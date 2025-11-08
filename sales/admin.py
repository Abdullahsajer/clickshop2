from django.contrib import admin
from .models import Cart, CartItem, Order, OrderItem

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    list_filter = ('product',)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1  # عرض وإضافة عناصر الطلب مباشرة داخل صفحة الطلب


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline]  # عرض العناصر داخل صفحة الطلب مباشرة


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')
    list_filter = ('order',)
