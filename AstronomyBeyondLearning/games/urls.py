from django.urls import path
from . import views 

app_name = "games"

urlpatterns = [
    path("", views.game, name="game"),
    path("multiple_choice_game/", views.multiple_choice_game, name="multiple_choice"),
    path("results/", views.results, name="results"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),


]