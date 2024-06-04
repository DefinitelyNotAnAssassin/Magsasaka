from django.shortcuts import render, redirect
from TransactionRecord.forms import TransactionRecordForm
# Create your views here.


def index(request):
    print(request.user)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            form = TransactionRecordForm()
            items = { 
                     'form': form
            }
            return render(request, 'LandingPage/admin_index.html', context = items)
        else:
            return redirect('virtual_id')
    else: 
        return render(request, 'LandingPage/index.html')



def admin_index(request, id):
    print(request.user)
    if request.user.is_authenticated:
        if request.user.is_superuser:
            form = TransactionRecordForm(initial={'beneficiary': id})
            
            
            items = { 
                     'form': form
            }
            return render(request, 'LandingPage/admin_index.html', context = items)
        else:
            return redirect('virtual_id')
    else: 
        return redirect('index')