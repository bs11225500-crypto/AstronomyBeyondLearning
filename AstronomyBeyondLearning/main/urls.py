from django.urls import path 
from . import views

app_name = 'main'



urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about_view, name="about_view"),
    path("messages/", views.contact_messages_view, name="contact_messages"),

]