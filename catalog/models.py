from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="اسم التصنيف")
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='children')

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "التصنيفات"
        ordering = ['name']

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="العلامة التجارية")
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "علامة تجارية"
        verbose_name_plural = "العلامات التجارية"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم المنتج")
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, verbose_name="وصف المنتج")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='products')
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    stock = models.PositiveIntegerField(default=0, verbose_name="المخزون")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "منتج"
        verbose_name_plural = "المنتجات"

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    alt_text = models.CharField(max_length=200, blank=True)

    class Meta:
        verbose_name = "صورة منتج"
        verbose_name_plural = "صور المنتجات"

    def __str__(self):
        return f"صورة لـ {self.product.name}"
