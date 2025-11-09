from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="اسم التصنيف")
    slug = models.SlugField(unique=True, verbose_name="الرابط (Slug)")
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='children',
        verbose_name="التصنيف الأب"
    )

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"
        ordering = ['name']

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم العلامة التجارية")
    slug = models.SlugField(unique=True, verbose_name="الرابط (Slug)")

    class Meta:
        verbose_name = "علامة تجارية"
        verbose_name_plural = "العلامات التجارية"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    slug = models.SlugField(unique=True, verbose_name="الرابط (Slug)")
    description = models.TextField(blank=True, verbose_name="وصف المنتج")
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='products',
        verbose_name="التصنيف"
    )
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products',
        verbose_name="العلامة التجارية"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    stock = models.PositiveIntegerField(default=0, verbose_name="المخزون")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', null=True, blank=True,
                              verbose_name="صورة المنتج")  # ✅ تمت الإضافة هنا
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإضافة")

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name
