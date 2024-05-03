from django.contrib import admin
from UserAuthentication.models import Account 
from django.contrib import admin
from UserAuthentication.models import Account

class AccountAdmin(admin.ModelAdmin):
    list_filter = (
       
        'region',
        'province',
        'district',
        'city_municipality',
        'barangay',
        'street',
        'house_no',
        
    )

admin.site.register(Account, AccountAdmin)
