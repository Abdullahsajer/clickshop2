from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product


class Cart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='carts',
        verbose_name="المستخدم"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الإنشاء")

    class Meta:
        verbose_name = "سلة تسوق"
        verbose_name_plural = "سلات التسوق"

    def __str__(self):
        return f"سلة المستخدم: {self.user.username if self.user else 'زائر'}"


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="السلة"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="المنتج"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")

    class Meta:
        verbose_name = "عنصر في السلة"
        verbose_name_plural = "عناصر السلة"

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'جديد'),
        ('paid', 'مدفوع'),
        ('shipped', 'تم الشحن'),
        ('delivered', 'تم التوصيل'),
        ('cancelled', 'ملغي'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name="المستخدم"
    )
    address = models.CharField(max_length=500, verbose_name="عنوان الشحن")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ الإجمالي")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name="حالة الطلب"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاريخ الطلب")

    class Meta:
        verbose_name = "طلب"
        verbose_name_plural = "الطلبات"

    def __str__(self):
        return f"طلب رقم {self.id} - المستخدم: {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="الطلب"
    )
    product = models.CharField(max_length=200, verbose_name="اسم المنتج")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")

    class Meta:
        verbose_name = "عنصر في الطلب"
        verbose_name_plural = "عناصر الطلب"

    def __str__(self):
        return f"{self.quantity} × {self.product}"
