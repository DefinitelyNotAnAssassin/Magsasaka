from django.urls import path 
from LandingPage import views

urlpatterns = [
    path('', views.index, name='index'),
]