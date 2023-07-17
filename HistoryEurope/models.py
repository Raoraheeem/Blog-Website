from django.db import models

class HistoryEurope(models.Model):
    Country_title=models.CharField(max_length=50)
    Country_desc=models.TextField()
    Country_img=models.FileField(upload_to="Blog/",max_length=250,null=True,default=None)

# Create your models here.
