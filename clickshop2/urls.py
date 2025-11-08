from django.contrib import admin
from django.urls import path, include  # ✅ include مطلوب لربط التطبيقات

urlpatterns = [
    path('admin/', admin.site.urls),

    # ✅ جعل تطبيق المنتجات هو الصفحة الرئيسية للموقع
    path('', include('catalog.urls')),           # الصفحة الرئيسية تعرض المنتجات

    # ✅ روابط التطبيقات الأخرى
    path('accounts/', include('accounts.urls')),  # تطبيق الحسابات والمستخدمين
    path('sales/', include('sales.urls')),        # تطبيق السلة والطلبات
]
