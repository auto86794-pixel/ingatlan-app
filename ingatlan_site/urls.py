from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # saját app
    path('', include('listings.urls')),

    # 🔐 Django auth (login, logout)
    path('accounts/', include('django.contrib.auth.urls')),
]