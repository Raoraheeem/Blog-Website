from django.db import models

class TravelEurope(models.Model):
    Place_name=models.CharField(max_length=50)
    Place_desc=models.TextField()
    Place_img=models.FileField(upload_to='Blog/',max_length=250,null=True,default=None)

# Create your models here.
