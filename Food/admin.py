from django.contrib import admin
from Food.models import Food
class FoodAdmin(admin.ModelAdmin):
  list_display=('Food_title','Food_desc','Food_img')
 
admin.site.register(Food,FoodAdmin)

# Register your models here.
