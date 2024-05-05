from django.shortcuts import render
from django.contrib.auth import login
from UserAuthentication.models import Account
# Create your views here.

def virtual_id(request):
<<<<<<< HEAD
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
=======
   try:
      signature = request.user.signature.url.replace('UserModule/', '')
   except: 
      signature = "https://media.istockphoto.com/vectors/no-image-available-icon-vector-id1216251206?k=20&m=1216251206&s=170667a&w=0&h=A72dFkHkDdSfmT6iWl6eMN9t_JZmqGeMoAycP-LMAw4="
   photo = request.user.photo.url.replace('UserModule/', '') 
   qr_code = request.user.qr_code.url.replace('UserModule/', '')
   items = { 
            'current_user': request.user,
               'signature': signature,
               'photo': photo,
               'qr_code': qr_code
            }
   return render(request, 'UserModule/virtual_id.html', context = items)
>>>>>>> 5f7ddb0089143ee8b8e248fcf7b8a2ef9ea622e3
