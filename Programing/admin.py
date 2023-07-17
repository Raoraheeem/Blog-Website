from django.contrib import admin
from Programing.models import Programing

class ProgramingAdmin(admin.ModelAdmin):
    list_display=('Topic_name','Topic_desc','Topic_img')
admin.site.register(Programing,ProgramingAdmin)

# Register your models here.
