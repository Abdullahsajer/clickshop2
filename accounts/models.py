from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, verbose_name="رقم الجوال")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="تاريخ الميلاد")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, verbose_name="الاسم الكامل")
    phone = models.CharField(max_length=20, verbose_name="رقم الجوال")
    city = models.CharField(max_length=100, verbose_name="المدينة")
    district = models.CharField(max_length=100, verbose_name="الحي")
    street = models.CharField(max_length=200, verbose_name="اسم الشارع")
    postal_code = models.CharField(max_length=10, verbose_name="الرمز البريدي")
    is_default = models.BooleanField(default=False, verbose_name="العنوان الافتراضي")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.city}"
