from django.shortcuts import render, redirect
from TransactionRecord.forms import TransactionRecordForm
from UserAuthentication.models import Account
# Create your views here.

def create_transaction(request): 
    if request.method == "GET": 
        
        items = { 
                'form': TransactionRecordForm()
                }
        return render(request, 'TransactionRecord/index.html', context = items)
    
    elif request.method == "POST": 
        post_data = request.POST.copy()  # Make a mutable copy
        try:
            account = Account.objects.get(bh_id=post_data.get('beneficiary'))
            post_data['beneficiary'] = account.id  # Replace 'beneficiary' with account instance
        except Account.DoesNotExist:
            print("Account does not exist")
            return redirect('index')
    
        form = TransactionRecordForm(post_data)
    
        if form.is_valid(): 
            form.save(commit=True)
            return redirect('index')
        else: 
            print(form.errors)
            items = { 
                'form': form
            }
            return redirect ('index')