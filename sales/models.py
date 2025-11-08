from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"سلة {self.user} - {self.created_at}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} × {self.product.name}"


class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'جديد'),
        ('paid', 'تم الدفع'),
        ('shipped', 'تم الشحن'),
        ('delivered', 'تم التوصيل'),
        ('cancelled', 'ملغي'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, verbose_name="عنوان الشحن")
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المجموع")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="الحالة")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"طلب #{self.id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} × {self.product}"
