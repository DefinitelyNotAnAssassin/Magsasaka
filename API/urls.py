from django.urls import path
from API import views

urlpatterns = [ 
            path('barangay_data', views.barangay_data, name = "barangay data"),
            path('age_data', views.age_data, name = "age data"),
            path('family_voters_data', views.family_voters_data, name = "family voters data"),
            path('get_locations', views.get_locations, name = "get locations"),
               ]