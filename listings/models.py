from django.db import models
from django.contrib.auth.models import User


# 🏠 INGATLAN
class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    title = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    price = models.IntegerField()
    size = models.IntegerField()
    rooms = models.IntegerField()
    description = models.TextField()

    # 📸 KÉPFELTÖLTÉS
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title


# ❤️ KEDVENCEK
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.listing.title}"