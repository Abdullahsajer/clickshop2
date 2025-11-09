from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from catalog.models import Product
from .models import Cart, CartItem, Order


# ✅ عرض سلة التسوق
@login_required
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {'cart': cart}
    return render(request, 'sales-templates/cart.html', context)


# ✅ إضافة منتج للسلة
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # التحقق من وجود العنصر نفسه في السلة
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        cart_item.quantity += 1  # زيادة الكمية إذا المنتج موجود بالفعل
    cart_item.save()

    return redirect('sales:cart')  # بعد الإضافة، الانتقال لصفحة السلة


# ✅ صفحة الدفع (Checkout)
@login_required
def checkout_view(request):
    cart = get_object_or_404(Cart, user=request.user)

    if request.method == 'POST':
        # إنشاء الطلب عند إتمام عملية الدفع
        order = Order.objects.create(
            user=request.user,
            address=request.POST.get('address', ''),
            total=sum(item.product.price * item.quantity for item in cart.items.all()),
        )

        # تحويل عناصر السلة إلى عناصر الطلب
        for item in cart.items.all():
            order.items.create(
                product=item.product.name,
                price=item.product.price,
                quantity=item.quantity
            )
        cart.items.all().delete()  # تفريغ السلة بعد إنشاء الطلب

        return redirect('sales:order_detail', order_id=order.id)

    return render(request, 'sales-templates/checkout.html', {'cart': cart})


# ✅ عرض تفاصيل طلب معين
@login_required
def order_detail_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'sales-templates/order_detail.html', {'order': order})
