from django.urls import path
from . import views

urlpatterns = [
    # 🟢 TEMP USER (FREE RENDER FIX)
    path('create-user/', views.create_test_user),

    # 🏠 FŐOLDAL
    path('', views.home, name='home'),

    # 🔍 DETAIL
    path('listing/<int:id>/', views.listing_detail, name='listing_detail'),

    # ➕ CREATE
    path('create/', views.create_listing, name='create'),

    # ✏️ EDIT
    path('edit/<int:id>/', views.edit_listing, name='edit_listing'),

    # ❌ DELETE
    path('delete/<int:id>/', views.delete_listing, name='delete_listing'),
]