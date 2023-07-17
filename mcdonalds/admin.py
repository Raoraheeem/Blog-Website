from django.contrib import admin
from mcdonalds.models import mcdonalds

class mcdonaldsAdmin(admin.ModelAdmin):
     list_display=('Food_title','Food_desc','Food_img')

admin.site.register(mcdonalds,mcdonaldsAdmin)

# Register your models here.
