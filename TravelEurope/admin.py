from django.contrib import admin
from TravelEurope.models import TravelEurope

class TravelEuropeAdmin(admin.ModelAdmin):
    list_display=('Place_name','Place_desc','Place_img')

admin.site.register(TravelEurope,TravelEuropeAdmin)

# Register your models here.
