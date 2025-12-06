from django.contrib import admin
from .models import QuizProgress


# Register your models here.
class QuizProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "attempts", "best_score", "last_score", "last_played")
    search_fields = ("user__username",)
    list_filter = ("last_played",)


admin.site.register(QuizProgress, QuizProgressAdmin)
