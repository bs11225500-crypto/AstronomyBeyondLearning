from django.urls import path 
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.log_out, name='log_out'),
    path('update/profile/', views.update_user_profile, name='update_profile'),
    path('<str:user_name>/posts/<str:post_type>/', views.user_posts_type_view, name="user_posts_type"),
    path('profile/<str:user_name>/', views.user_profile_view, name='user_profile_view'),
    path("profile/<str:username>/saved-planets/", views.saved_planets_in_profile, name="saved_planets"),



]

