from django.shortcuts import render
from django.contrib.auth import login
from UserAuthentication.models import Account
# Create your views here.

def virtual_id(request):
    signature = request.user.signature.url.replace('/BagongHenerasyon/UserModule/', '')
    photo = request.user.photo.url.replace('/BagongHenerasyon/UserModule/', '')
    qr_code = request.user.qr_code.url.replace('/BagongHenerasyon/UserModule/', '')
    items = {
             'current_user': request.user,
                'signature': signature,
                'photo': photo,
                'qr_code': qr_code
             }
    return render(request, 'UserModule/virtual_id.html', context = items)