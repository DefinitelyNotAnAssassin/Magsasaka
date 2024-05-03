from django.db import models

# Create your models here.


class TransactionRecord(models.Model): 
    beneficiary = models.ForeignKey("UserAuthentication.account", on_delete=models.CASCADE)
    date = models.DateField()
    service = models.CharField(max_length=255)
    remarks = models.TextField()