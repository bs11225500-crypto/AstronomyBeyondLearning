from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class QuizProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    attempts = models.IntegerField(default=0)
    best_score = models.IntegerField(default=0)
    last_score = models.IntegerField(default=0)
    last_played = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Progress"