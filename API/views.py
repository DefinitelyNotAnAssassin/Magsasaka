from django.shortcuts import render
from django.http import JsonResponse
from UserAuthentication.models import Account
from ph_geography.models import Barangay, Municipality
import json
# Create your views here.

QUEZON_CITY = Municipality.objects.get(name = "QUEZON CITY")
BARANGAYS = Barangay.objects.filter(municipality = QUEZON_CITY)
def barangay_data(request):
    data = {}
    for barangay in BARANGAYS:
        account_count = Account.objects.filter(barangay=barangay).count()
        if account_count > 0:
            data[barangay.name] = account_count
        
    print(data)
    return JsonResponse(json.dumps(data), safe = False)
    
    
