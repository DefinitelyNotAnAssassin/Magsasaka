from django.shortcuts import render, redirect
from django.contrib.auth import login
from UserAuthentication.models import Account

def virtual_id(request):
  if request.user.is_authenticated:
    try:
      signature = request.user.signature.url.replace('UserModule/', '')
    except Exception as e:
      signature = "https://www.drodd.com/images14/white13.png"
    
    try:
      photo = request.user.photo.url.replace('UserModule/', '')
    except Exception as e:
      photo = "https://www.drodd.com/images14/white13.png"
   
    try:
      qr_code = request.user.qr_code.url.replace('UserModule/', '')
    except Exception as e:
      print(f"Error retrieving QR code: {e}")
\
    
    items = {
      'current_user': request.user,
      'signature': signature,
      'photo': photo,
      'qr_code': qr_code
    }
    return render(request, 'UserModule/virtual_id.html', context=items)
  else:
    return redirect('index')
