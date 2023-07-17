from django.contrib import admin
from HistoryAsia.models import HistoryAsia

class HistoryAsiaAdmin(admin.ModelAdmin):
    list_display=('Country_title','Country_desc','Country_img')

admin.site.register(HistoryAsia,HistoryAsiaAdmin)

# Register your models here.
