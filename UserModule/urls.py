from django.urls import path 
from UserModule import views 

urlpatterns = [
    path('virtual_id', views.virtual_id, name='virtual_id'),
]