from django.contrib import admin
from TravelAsia.models import TravelAsia

class TravelAsiaAdmin(admin.ModelAdmin):
    list_display=('Place_name','Place_desc','Place_img')

admin.site.register(TravelAsia,TravelAsiaAdmin)

# Register your models here.
