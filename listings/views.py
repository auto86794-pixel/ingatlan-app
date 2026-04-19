from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
import cloudinary.uploader


# 🔹 HOME
def home(request):
    return render(request, 'home.html')


# 🔹 REGISTER
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


# 🔥 CREATE LISTING + CLOUDINARY
@login_required
def create_listing(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('image')

        if image:
            result = cloudinary.uploader.upload(image)
            image_url = result.get('secure_url')
            print("CLOUDINARY URL:", image_url)

        # később itt mentjük adatbázisba
        return redirect('home')

    return render(request, 'create_listing.html')


# 🔹 LISTING DETAIL
def listing_detail(request, id):
    return render(request, 'listing_detail.html')


# 🔹 EDIT LISTING
@login_required
def edit_listing(request, id):
    return render(request, 'edit_listing.html')


# 🔹 DELETE LISTING
@login_required
def delete_listing(request, id):
    return redirect('home')