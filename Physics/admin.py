from django.contrib import admin
from Physics.models import Physics

class PhysicsAdmin(admin.ModelAdmin):
    list_display=('Topic_name','Topic_desc','Topic_img')
admin.site.register(Physics,PhysicsAdmin)

# Register your models here.
