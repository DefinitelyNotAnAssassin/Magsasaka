from django.shortcuts import render, redirect
from django.contrib.auth import login
from UserAuthentication.models import Account

def virtual_id(request):
  if request.user.is_authenticated:
    try:
      signature = request.user.signature.url.replace('UserModule/', '')
    except Exception as e:
<<<<<<< HEAD
      signature = "https://cdn.wallpapersafari.com/15/64/s0zmcy.jpg"

    try:
      photo = request.user.photo.url.replace('UserModule/', '')
    except Exception as e:
      photo = "https://cdn.wallpapersafari.com/15/64/s0zmcy.jpg"

    try:
      qr_code = request.user.qr_code.url.replace('UserModule/', '')
    except Exception as e:
      qr_code = "https://cdn.wallpapersafari.com/15/64/s0zmcy.jpg"

=======
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
    
>>>>>>> 4b5f5284dd4223889a1b7af21630e11eeb4daf7c
    items = {
      'current_user': request.user,
      'signature': signature,
      'photo': photo,
      'qr_code': qr_code
    }
    return render(request, 'UserModule/virtual_id.html', context=items)
  else:
    return redirect('index')
