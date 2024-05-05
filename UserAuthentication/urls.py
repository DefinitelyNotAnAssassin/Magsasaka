from django.urls import path 
from UserAuthentication import views 

urlpatterns = [ 
               path('register', views.register, name='register'),
               path('login', views.login, name='login'),
               path('logout', views.logout, name ='logout'),
               path('verification/<str:bh_id>', views.verification, name = 'verification'),
               path('resend_verification/<str:bh_id>', views.resend_verification, name = 'resend_verification')
               ]