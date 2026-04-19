from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Listing
import cloudinary.uploader


# 🟢 IDEIGLENES USER LÉTREHOZÁS (FREE RENDER FIX)
def create_test_user(request):
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            password='12345678Aa'
        )
        return HttpResponse("User létrehozva")
    return HttpResponse("Már létezik")


# 🏠 LISTA
def home(request):
    listings = Listing.objects.all()
    return render(request, 'home.html', {'listings': listings})


# 🔍 RÉSZLETEK
def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'detail.html', {'listing': listing})


# ➕ CREATE
@login_required(login_url='/accounts/login/')
def create_listing(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        image_url = None

        if image:
            result = cloudinary.uploader.upload(image)
            image_url = result.get('secure_url')

        Listing.objects.create(
            title=title,
            description=description,
            price=price,
            image=image_url,
            user=request.user
        )

        return redirect('/')

    return render(request, 'create_listing.html')


# ✏️ EDIT
@login_required(login_url='/accounts/login/')
def edit_listing(request, id):
    listing = get_object_or_404(Listing, id=id)

    if request.method == 'POST':
        listing.title = request.POST.get('title')
        listing.description = request.POST.get('description')
        listing.price = request.POST.get('price')

        if request.FILES.get('image'):
            result = cloudinary.uploader.upload(request.FILES.get('image'))
            listing.image = result.get('secure_url')

        listing.save()
        return redirect('/')

    return render(request, 'edit_listing.html', {'listing': listing})


# ❌ DELETE
@login_required(login_url='/accounts/login/')
def delete_listing(request, id):
    listing = get_object_or_404(Listing, id=id)
    listing.delete()
    return redirect('/')