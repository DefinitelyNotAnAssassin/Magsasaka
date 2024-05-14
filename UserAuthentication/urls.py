from django.urls import path 
from UserAuthentication import views 

urlpatterns = [ 
               path('register', views.register, name='register'),
               path('login', views.login, name='login'),
               path('logout', views.logout, name ='logout'),
               path('edit_profile', views.edit_profile, name = 'edit_profile'),
               path('verification/<str:bh_id>', views.verification, name = 'verification'),
               path('resend_verification/<str:bh_id>', views.resend_verification, name = 'resend_verification'),
               path('getProvinces', views.getProvinces, name = 'getProvinces'),
               path('getCities', views.getCities, name = 'getCities'),
               path('getBarangays', views.getBarangays, name = 'getBarangays'),
               path('checkUsername', views.checkUsername, name = 'checkUsername'),
               ]