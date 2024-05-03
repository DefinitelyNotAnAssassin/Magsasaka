from django.urls import path
from API import views

urlpatterns = [ 
            path('barangay_data', views.barangay_data, name = "barangay data")
               ]