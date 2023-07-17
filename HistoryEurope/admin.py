from django.contrib import admin
from HistoryEurope.models import HistoryEurope

class HistoryEuropeAdmin(admin.ModelAdmin):
    list_display=('Country_title','Country_desc','Country_img')

admin.site.register(HistoryEurope,HistoryEuropeAdmin)

# Register your models here.
