from django.db import models

class Food(models.Model):
    Food_title=models.CharField(max_length=50)
    Food_desc=models.TextField()
    Food_img=models.FileField(upload_to="Blog/",max_length=250,null=True, default=None)

# Create your models here.
