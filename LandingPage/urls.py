from django.urls import path 
from LandingPage import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:id>', views.admin_index, name='admin index')
]