from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Brand, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price', 'stock', 'is_active', 'image_preview', 'created_at')
    list_filter = ('category', 'brand', 'is_active')
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ('image_preview', 'created_at')

    fieldsets = (
        ('معلومات المنتج', {
            'fields': ('name', 'slug', 'description')
        }),
        ('التصنيفات والارتباطات', {
            'fields': ('category', 'brand')
        }),
        ('السعر والمخزون', {
            'fields': ('price', 'stock', 'is_active')
        }),
        ('صورة المنتج', {
            'fields': ('image', 'image_preview')
        }),
        ('معلومات إضافية', {
            'fields': ('created_at',)
        }),
    )

    def image_preview(self, obj):
        """عرض معاينة للصورة داخل لوحة التحكم"""
        if obj.image:
            return format_html('<img src="{}" width="70" style="border-radius:6px;" />', obj.image.url)
        return "لا توجد صورة"
    image_preview.short_description = "معاينة"


# ✅ إخفاء نموذج الصور القديم إذا كان مسجلًا (اختياري)
# admin.site.unregister(ProductImage)
