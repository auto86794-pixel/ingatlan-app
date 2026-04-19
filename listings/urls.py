from django.urls import path
from . import views

urlpatterns = [
    # 🏠 FŐOLDAL
    path('', views.home),

    # 📄 INGATLAN DETAIL
    path('listing/<int:id>/', views.detail),

    # ❤️ KEDVENCEK
    path('favorite/<int:id>/', views.toggle_favorite),
    path('favorites/', views.favorites_page),

    # 🔐 USER
    path('register/', views.register),
    path('profile/', views.profile),

    # ✏️ SZERKESZTÉS
    path('edit/<int:id>/', views.edit_listing),

    # ➕ ÚJ HIRDETÉS
    path('create/', views.create_listing),

    # 🗑️ TÖRLÉS
    path('delete/<int:id>/', views.delete_listing),
]