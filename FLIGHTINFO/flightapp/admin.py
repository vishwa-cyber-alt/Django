#from django.contrib import admin

# Register your models here.
# Register your models here.

from django.contrib import admin
from flightapp.models import Flightinfo

#Flightnumber
class FlightinfoAdmin(admin.ModelAdmin):
    Flightinfo_details = ['Flightnumber', 'Destination', 'Distance', 'Fuelquantity']


admin.site.register(Flightinfo)
