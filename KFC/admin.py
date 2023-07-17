from django.contrib import admin
from KFC.models import KFC

class KFCAdmin(admin.ModelAdmin):
    list_display=('Food_title','Food_desc','Food_img')

admin.site.register(KFC,KFCAdmin)

# Register your models here.
