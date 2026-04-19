from django.contrib import admin
from django.urls import path, include
from listings import views


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # 🔐 Django auth (LOGIN / LOGOUT / PASSWORD stb.)
    path('accounts/', include('django.contrib.auth.urls')),

    # 🏠 főoldal
    path('', views.home, name='home'),

    # 👤 regisztráció
    path('register/', views.register, name='register'),

    # ➕ új hirdetés
    path('create/', views.create_listing, name='create'),

    # 📄 hirdetés részletek
    path('listing/<int:id>/', views.listing_detail, name='listing_detail'),

    # ✏️ szerkesztés
    path('edit/<int:id>/', views.edit_listing, name='edit_listing'),

    # ❌ törlés
    path('delete/<int:id>/', views.delete_listing, name='delete_listing'),
]