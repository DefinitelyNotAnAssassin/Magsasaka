from io import BytesIO
from uuid import uuid4
import qrcode
from django.contrib.auth import login as login_user, authenticate, logout as logout_user
from django.core.files import File
from django.shortcuts import render, redirect
from UserAuthentication.forms import UserForm, LoginForm, EditProfileForm
from UserAuthentication.models import Account
from twilio.rest import Client
from ph_geography.models import Municipality, Province, Barangay
import django.contrib.messages as messages
from django.http import JsonResponse
import json

account_sid = "AC6a108c9149464864b9e8d87cca74a323"
auth_token = "a1d933e79bca8553c28f59c0f4a38c2f"
client = Client(account_sid, auth_token)


# Create your views here.
def verify_user_code(phone_number, code):
    try:
        verification_check = client.verify.services('VAea94f418f41f18ed40c27bb98c833dff') \
            .verification_checks \
            .create(to=phone_number, code=code)

    except Exception as e:
        return verification_check.status == "approved"

    return verification_check.status == "approved"


def resend_verification(request, bh_id):
    try:
        account = Account.objects.get(bh_id = bh_id)
        verification = client.verify.services('VAea94f418f41f18ed40c27bb98c833dff') \
        .verifications \
        .create(to=f'{account.contact_number}', channel='sms')

        return redirect('verification', bh_id)

    except:
        return redirect('index')

def register(request):
    if request.method == "GET":

        items = {
                'form': UserForm()
        }
        return render(request, 'UserAuthentication/register.html', context = items)

    if request.method == "POST":
        try:
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.bh_id = f'{user.first_name} {user.last_name} - {user.barangay}-{uuid4()}'
                user.isVerified = True
                user.contact_number = '+63' + user.contact_number[1:] if user.contact_number.startswith('0') else user.contact_number
                qr = qrcode.make(user.bh_id)
                qr_io = BytesIO()
                qr.save(qr_io, format='PNG')
                qr_io.seek(0)

                user.qr_code.save(f'{user.bh_id}.png', File(qr_io), save=False)
                longitude = request.POST.get('longitude')
                if longitude != '':
                    user.longitude = longitude
                else:
                    user.longitude = 121.05090000

                latitude = request.POST.get('latitude')
                if latitude != '':
                    user.latitude = latitude
                else:
                    user.latitude = 14.64880000
                user.save()
                form.save()
                login_user(request, user)



                return redirect('virtual_id')
        except Exception as e:
            print(e)
            return redirect('virtual_id')

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
        try:
            form = LoginForm(request.POST)
            authenticated_user = authenticate(username = form.data['username'], password = form.data['password'])
            if authenticated_user is not None:

                if authenticated_user.isVerified == False and not authenticated_user.is_superuser:
                    return redirect('verification', authenticated_user.bh_id)
                elif authenticated_user.is_superuser:
                    login_user(request, authenticated_user)
                    return redirect('admin_index')
                else:
                    login_user(request, authenticated_user)
                    return redirect('virtual_id')
            else:
                items = {
                    'form': form
                }
                messages.error(request, 'Invalid username or password')

            return render(request, 'UserAuthentication/login.html', context = items)

        except:
            return redirect('index')

def edit_profile(request):
    if request.method == "GET":

        items = {
            'form': EditProfileForm(instance=request.user)
        }
        return render(request, 'UserAuthentication/edit_profile.html', context = items)
    elif request.method == "POST":
        try:
            form = EditProfileForm(request.POST, request.FILES, instance=request.user)
            if form.is_valid():
                user = form.save(commit=False)
                user.contact_number = '+63' + user.contact_number[1:] if user.contact_number.startswith('0') else user.contact_number
                user.save()
                form.save()
                return redirect('virtual_id')
            else:
                items = {
                    'form': form
                }
                return render(request, 'UserAuthentication/edit_profile.html', context = items)
        except Exception as e:

            return redirect('virtual_id')


def logout(request):
    logout_user(request)
    return redirect('index')


def verification(request, bh_id = None):

    if request.user.is_authenticated:
        return redirect('virtual_id')
    if request.method == "GET" and not bh_id == None:
        try:
            account = Account.objects.get(bh_id = bh_id)

            if not account.isVerified:
                items = {
                        'account': account}
                return render(request, "UserAuthentication/verification.html", context=items)
            else:
                login_user(account)
                return redirect('index')
        except:
            return redirect('index')

    elif request.method == "POST":
        try:
            data = request.POST
            OTP = data.get('OTP')
            account = Account.objects.get(bh_id = bh_id)
            print(OTP)
            if verify_user_code(phone_number=account.contact_number, code = OTP):
                account.isVerified = True
                account.save()
                login_user(request, account)
                return redirect('virtual_id')
            else:
                return redirect('verification', account.bh_id)
        except:
            return redirect('index')
    else:
        return redirect('index')



def getProvinces(request):
    region = request.GET.get('region')

    provinces = Province.objects.filter(region__pk = region)
    return JsonResponse(list(provinces.values()), safe=False)

def getCities(request):
    province = request.GET.get('province')
    cities = Municipality.objects.filter(province__name = province)
    return JsonResponse(list(cities.values()), safe=False)
def getBarangays(request):
    city = request.GET.get('city')
    barangays = Barangay.objects.filter(municipality_id__name = city)
    return JsonResponse(list(barangays.values()), safe=False)



def checkUsername(request):
    # check if the username exists, if it is return true, if its not then false in a jsonresponse

    if request.method == "POST":
        data = request.body.decode('utf-8')
        data_dict = json.loads(data)
        username = data_dict['username']
        if Account.objects.filter(username=username).exists():
            return JsonResponse({'username_exists': 'true'}, status=200)
        else:
            return JsonResponse({'username_exists': 'false'}, status=200)

    return JsonResponse({'error': 'Invalid method'}, status=400)

