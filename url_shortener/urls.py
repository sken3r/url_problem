from django.urls import path

from url_shortener import views

urlpatterns = [path("shorten_url/", views.shorten_url)]
