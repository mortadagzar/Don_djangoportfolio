from django.db import models

# Create your models here.
class Post(models.Model):
       title = models.CharField(max_length = 50)
       discription = models.CharField(max_length = 50)
       picture = models.ImageField(upload_to = 'pictures')
