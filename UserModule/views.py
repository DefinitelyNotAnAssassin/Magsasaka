from django.shortcuts import render, redirect
from django.contrib.auth import login
from UserAuthentication.models import Account
# Create your views here.

def virtual_id(request):
    if request.user.is_authenticated:
        try:
          signature = request.user.signature.url.replace('UserModule/', '')
        except:
          signature = "https://www.drodd.com/images14/white2.jpg"
        photo = request.user.photo.url.replace('UserModule/', '')
        qr_code = request.user.qr_code.url.replace('UserModule/', '')
        items = {
                'current_user': request.user,
                   'signature': signature,
                   'photo': photo,
                   'qr_code': qr_code
                }
        return render(request, 'UserModule/virtual_id.html', context = items)

    else:
        return redirect('index')
