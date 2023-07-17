from django.contrib import admin
from TravelAustralia.models import TravelAustralia

class TravelAustraliaAdmin(admin.ModelAdmin):
      list_display=('Place_name','Place_desc','Place_img')

admin.site.register(TravelAustralia,TravelAustraliaAdmin)
     

# Register your models here.
