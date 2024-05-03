from django.contrib import admin
from ph_geography.models import Region, Province, Municipality, Barangay  
# Register your models here.

admin.site.register(Region)
admin.site.register(Province)
admin.site.register(Municipality)
admin.site.register(Barangay)