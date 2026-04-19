from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from listings import views  # 👉 a te appod view-jai

urlpatterns = [
    # 🔹 ADMIN
    path('admin/', admin.site.urls),

    # 🔹 FŐOLDAL (listings)
    path('', views.home, name='home'),

    # 🔹 LISTINGS APP ROUTES (ha van külön urls.py-d)
    # path('', include('listings.urls')),  # csak akkor ha használod

    # 🔹 REGISZTRÁCIÓ
    path('register/', views.register, name='register'),

    # 🔥 LOGIN
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    # 🔥 LOGOUT
    path('accounts/logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), name='logout'),

    # 🔹 EGYÉB ROUTE-OK (példák, ha nálad is vannak)
    path('create/', views.create_listing, name='create'),
    path('listing/<int:id>/', views.listing_detail, name='listing_detail'),
    path('edit/<int:id>/', views.edit_listing, name='edit'),
    path('delete/<int:id>/', views.delete_listing, name='delete'),
]