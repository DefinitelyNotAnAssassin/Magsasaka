from io import BytesIO
from django.shortcuts import render, redirect
from UserAuthentication.forms import UserForm, LoginForm
from django.contrib.auth import login as login_user, authenticate, logout as logout_user
from UserAuthentication.models import Account

import django.contrib.messages as messages
from django.core.files import File
import qrcode
from uuid import uuid4
from twilio.rest import Client 
from django.contrib.auth.hashers import make_password


def register(request):
    if request.method == "GET":
        
        items = { 
                'form': UserForm()
        }
        return render(request, 'UserAuthentication/register.html', context = items)

    if request.method == "POST": 
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.bh_id = f'{user.barangay}-{uuid4()}'
            qr = qrcode.make(user.bh_id)
            qr_io = BytesIO()
            qr.save(qr_io, format='PNG')
            qr_io.seek(0)

            # Assign the QR code image to the model's file field
            user.qr_code.save(f'{user.bh_id}.png', File(qr_io), save=False)

            # Now you can save the user instance, and the file will be committed
            user.save()
            form.save()

            user.save()
            form.save()
            
            verification = client.verify.services('VAea94f418f41f18ed40c27bb98c833dff') \
            .verifications \
            .create(to=f'{user.contact_number}', channel='sms')


            
            
            return redirect('verification', user.bh_id)
        else:
            items = {}
            items['form'] = form
            print(form.errors)
            
            return render(request, 'UserAuthentication/register.html', context = items)


def login(request):
    if request.method == "GET":
        items = {
            'form': LoginForm()
        }
    
        return render(request, 'UserAuthentication/login.html', context = items)
    elif request.method == "POST":
        form = LoginForm(request.POST)
        authenticated_user = authenticate(username = form.data['username'], password = form.data['password'])
        if authenticated_user is not None:
            
            if authenticated_user.isVerified == False:
                return redirect('verification', authenticated_user.bh_id)
            else:
                login_user(request, authenticated_user)
                return redirect('index')
            
            
        else:
            items = {
                'form': form
            }
            messages.error(request, 'Invalid username or password')
            
          
            
            return render(request, 'UserAuthentication/login.html', context = items)
        
        
        
def logout(request): 
    logout_user(request) 
    return redirect('index')


def verification(request, bh_id = None):
    if request.method == "GET" and not bh_id == None: 
        account = Account.objects.get(bh_id = bh_id)
        
        if not account.isVerified: 
            items = { 
                     'account': account}
            return render(request, "UserAuthentication/verification.html", context=items)
        else: 
            login_user(account)
            return redirect('index')
        
    elif request.method == "POST": 
        data = request.POST 
        OTP = data.get('OTP') 
        account = Account.objects.get(bh_id = bh_id) 
        print(OTP)
        if verify_user_code(phone_number=account.contact_number, code = OTP): 
            account.isVerified = True 
            account.save()
            return redirect('login')
        else:
            return redirect('verification', account.bh_id)
    else: 
        return redirect('index')
    
    
        