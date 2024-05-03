from django.urls import path 
from TransactionRecord import views
urlpatterns = [
    path('create_transaction', views.create_transaction, name = "create transaction")
]