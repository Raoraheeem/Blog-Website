from django.contrib import admin
from HistoryAmerica.models import HistoryAmerica

class HistoryAmericaAdmin(admin.ModelAdmin):
    list_display=('Country_title','Country_desc','Country_img')

admin.site.register(HistoryAmerica,HistoryAmericaAdmin)
# Register your models here.
