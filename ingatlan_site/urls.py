from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # login / logout
    path('accounts/', include('django.contrib.auth.urls')),

    # SAJÁT APP
    path('', include('listings.urls')),
]