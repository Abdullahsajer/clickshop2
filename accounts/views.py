from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from django.contrib.auth import logout

# ✅ تسجيل مستخدم جديد
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        phone = request.POST.get("phone")

        if User.objects.filter(username=username).exists():
            messages.error(request, "اسم المستخدم مستخدم بالفعل.")
            return redirect("accounts:register")

        if User.objects.filter(email=email).exists():
            messages.error(request, "البريد الإلكتروني مستخدم بالفعل.")
            return redirect("accounts:register")

        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, phone=phone)

        login(request, user)
        return redirect("home")  # ✅ بعد التسجيل ينتقل للصفحة الرئيسية

    return render(request, "accounts-templates/register.html")


# ✅ تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        identifier = request.POST.get("identifier")
        password = request.POST.get("password")

        user = authenticate(request, username=identifier, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "بيانات غير صحيحة، حاول مرة أخرى.")

    return render(request, "accounts-templates/login.html")

# ✅ تسجيل الخروج
def logout_view(request):
    logout(request)
    return redirect('home')