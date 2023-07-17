from django.db import models

class Programing(models.Model):
    Topic_name=models.CharField(max_length=50)
    Topic_desc=models.TextField()
    Topic_img=models.FileField(upload_to='Blog/',max_length=250,null=True,default=None)

# Create your models here.
