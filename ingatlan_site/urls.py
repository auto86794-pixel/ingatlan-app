from django.contrib import admin
from django.urls import path, include
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # főoldal + listings app
    path('', include('listings.urls')),

    # 🔥 REGISZTRÁCIÓ
    path('register/', views.register, name='register'),

    # 🔐 LOGIN / LOGOUT (django built-in)
    path('accounts/', include('django.contrib.auth.urls')),
]