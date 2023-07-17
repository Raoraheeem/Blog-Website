from django.contrib import admin
from Chemistry.models import Chemistry

class ChemistryAdmin(admin.ModelAdmin):
    list_display=('Topic_name','Topic_desc','Topic_img')
admin.site.register(Chemistry,ChemistryAdmin)

# Register your models here.
