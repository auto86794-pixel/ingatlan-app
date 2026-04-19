from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Listing, Favorite
from .forms import ListingForm


# 🏠 FŐOLDAL
def home(request):
    listings = Listing.objects.all()

    city = request.GET.get('city')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    order = request.GET.get('order')

    if city:
        listings = listings.filter(city__icontains=city)

    if min_price:
        try:
            listings = listings.filter(price__gte=int(min_price))
        except:
            pass

    if max_price:
        try:
            listings = listings.filter(price__lte=int(max_price))
        except:
            pass

    if order == 'low':
        listings = listings.order_by('price')
    elif order == 'high':
        listings = listings.order_by('-price')

    if request.user.is_authenticated:
        favorites = set(
            Favorite.objects.filter(user=request.user)
            .values_list('listing_id', flat=True)
        )
    else:
        favorites = set()

    return render(request, 'home.html', {
        'listings': listings,
        'favorites': favorites
    })


# 📄 DETAIL
def detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request, 'detail.html', {'listing': listing})


# ❤️ KEDVENC BE/KI
def toggle_favorite(request, id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    listing = get_object_or_404(Listing, id=id)

    favorite, created = Favorite.objects.get_or_create(
        user=request.user,
        listing=listing
    )

    if not created:
        favorite.delete()

    return redirect('/')


# ❤️ KEDVENCEK OLDAL
def favorites_page(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    listings = Listing.objects.filter(favorite__user=request.user)

    return render(request, 'favorites.html', {
        'listings': listings
    })


# 🆕 REGISZTRÁCIÓ
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


# 👤 PROFIL
def profile(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    listings = Listing.objects.filter(user=request.user)

    return render(request, 'profile.html', {
        'listings': listings
    })


# ✏️ SZERKESZTÉS
def edit_listing(request, id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    listing = get_object_or_404(Listing, id=id)

    if listing.user != request.user:
        return redirect('/')

    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing)
        if form.is_valid():
            form.save()
            return redirect('/profile/')
    else:
        form = ListingForm(instance=listing)

    return render(request, 'edit_listing.html', {
        'form': form
    })


# ➕ ÚJ HIRDETÉS
def create_listing(request):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect('/profile/')
    else:
        form = ListingForm()

    return render(request, 'create_listing.html', {
        'form': form
    })


# 🗑️ TÖRLÉS
def delete_listing(request, id):
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')

    listing = get_object_or_404(Listing, id=id)

    # 🔐 csak a tulaj törölhet
    if listing.user != request.user:
        return redirect('/')

    if request.method == 'POST':
        listing.delete()
        return redirect('/profile/')

    return redirect('/profile/')