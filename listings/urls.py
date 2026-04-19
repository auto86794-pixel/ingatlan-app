from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 🛠 ADMIN
    path('admin/', admin.site.urls),

    # 🔐 LOGIN / LOGOUT (Django beépített)
    path('accounts/', include('django.contrib.auth.urls')),

    # 🏠 SAJÁT APP (EZ A KULCS!)
    path('', include('listings.urls')),
]