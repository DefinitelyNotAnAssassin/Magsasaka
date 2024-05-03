from django.shortcuts import render
from TransactionRecord.forms import TransactionRecordForm
# Create your views here.

def create_transaction(request): 
    items = { 
             'form': TransactionRecordForm()
             }
    return render(request, 'TransactionRecord/index.html', context = items)