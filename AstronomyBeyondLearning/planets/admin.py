from django.contrib import admin
from .models import Planet, BookmarkPlanet


class PlanetAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "distance_from_sun",
        "radius",
        "gravity",
        "temperature",
        "moons_count",
    )

    search_fields = (
        "name",
        "description",
        "atmosphere",
    )

    list_filter = (
        "category",
        "moons_count",
    )


class BookmarkPlanetAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "planet",
        "created_at",
    )

    search_fields = (
        "user__username",
        "planet__name",
    )

    list_filter = (
        "created_at",
        "planet",
    )


admin.site.register(Planet, PlanetAdmin)
admin.site.register(BookmarkPlanet, BookmarkPlanetAdmin)

