from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Planet(models.Model):

    PLANET_CATEGORIES = [
        ('terrestrial', 'Terrestrial'),
        ('gas_giant', 'Gas Giant'),
        ('ice_giant', 'Ice Giant'),
        ('dwarf', 'Dwarf Planet'),
    ]
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='planets/', blank=True, null=True)
    description = models.TextField()
    distance_from_sun = models.CharField(max_length=100, blank=True)
    radius = models.CharField(max_length=100, blank=True)
    gravity = models.CharField(max_length=100, blank=True)
    day_length = models.CharField(max_length=100, blank=True)
    atmosphere = models.CharField(max_length=200, blank=True)
    temperature = models.CharField(max_length=50, blank=True)
    category = models.CharField(max_length=20, choices=PLANET_CATEGORIES, default='terrestrial')
    moons_count = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.name
    
class BookmarkPlanet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} bookmarked {self.planet.name}"
