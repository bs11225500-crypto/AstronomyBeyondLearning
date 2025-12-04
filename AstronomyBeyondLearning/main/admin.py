from django.contrib import admin
from .models import ContactMessage

# Register your models here.



class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "accepted_terms", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone", "message")
    list_filter = ("accepted_terms", "created_at")


admin.site.register(ContactMessage, ContactMessageAdmin)
