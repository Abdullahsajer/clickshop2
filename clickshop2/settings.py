from pathlib import Path

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح التشفير (يجب تغييره في بيئات الإنتاج)
SECRET_KEY = 'django-insecure-mwrbq76gclmb8ykb=70@3^0*-e-d(!wxgc17&7bfsp1+86g3&y'

# وضع التطوير
DEBUG = True

# العناوين المسموح بها
ALLOWED_HOSTS = []


# التطبيقات المثبتة
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ✅ تطبيقات المشروع المخصصة
    'accounts',    # إدارة المستخدمين والحسابات
    'catalog',     # المنتجات والتصنيفات
    'sales',       # السلة والطلبات والدفع
]


# الوسائط الوسطية Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ملف URLs الجذري
ROOT_URLCONF = 'clickshop2.urls'


# إعدادات الـ Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',  # ✅ مجلد القوالب الرئيسي لمسارك الجديد
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# WSGI
WSGI_APPLICATION = 'clickshop2.wsgi.application'


# قاعدة البيانات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# اللغة والوقت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_TZ = True


# الملفات الثابتة (static)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # ✅ مجلد للملفات الثابتة العامة (CSS, JS, IMG)
]


# تعريف تلقائي للأعمدة المبدئية في الـ Models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
