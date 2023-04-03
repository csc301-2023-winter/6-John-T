from django.db import models

# Create your models here.
class Park(models.Model):
    park_id = models.AutoField(primary_key=True) #PK 
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)