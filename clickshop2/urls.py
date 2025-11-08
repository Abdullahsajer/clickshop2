from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # لوحة التحكم
    path('admin/', admin.site.urls),

    # ✅ جعل تطبيق المنتجات هو الصفحة الرئيسية للموقع
    path('', include('catalog.urls')),  # الصفحة الرئيسية: عرض المنتجات

    # ✅ روابط التطبيقات الأخرى
    path('accounts/', include('accounts.urls')),  # تطبيق الحسابات والمستخدمين
    path('sales/', include('sales.urls')),        # تطبيق السلة والطلبات
]

# ✅ دعم ملفات الوسائط (Media) والملفات الثابتة (Static) أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
