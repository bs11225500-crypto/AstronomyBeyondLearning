from django.contrib import admin
from .models import UserProfile
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "bio", "website")   
    search_fields = ("user__username", "bio")
    list_filter = ("user",)  


admin.site.register(UserProfile, UserProfileAdmin)
