from django.urls import path
from . import views

urlpatterns = [
    # 🟢 TEMP USER
    path('create-user/', views.create_test_user),

    # 🏠 FŐOLDAL
    path('', views.home),

    # 🔍 DETAIL
    path('listing/<int:id>/', views.listing_detail),

    # ❤️ KEDVENC
    path('favorite/<int:id>/', views.toggle_favorite),
    path('favorites/', views.favorites_page),

    # 👤 USER
    path('register/', views.register),
    path('profile/', views.profile),

    # ✏️ EDIT
    path('edit/<int:id>/', views.edit_listing),

    # ➕ CREATE
    path('create/', views.create_listing),

    # ❌ DELETE
    path('delete/<int:id>/', views.delete_listing),
]