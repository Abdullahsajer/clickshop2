from django.contrib import admin
from .models import Category, Brand, Product, ProductImage

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # عدد الحقول الإضافية لإضافة الصور


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'stock', 'is_active', 'created_at')
    list_filter = ('category', 'brand', 'is_active')
    search_fields = ('name', 'description')
    inlines = [ProductImageInline]  # عرض الصور داخل صفحة المنتج مباشرة


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image')
