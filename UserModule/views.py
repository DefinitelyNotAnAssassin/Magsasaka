from django.shortcuts import render
from django.contrib.auth import login
from UserAuthentication.models import Account 
# Create your views here.

def virtual_id(request):
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