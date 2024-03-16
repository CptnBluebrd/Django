from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='articles-home'),
    path('about/', views.about, name='about-me'),
]