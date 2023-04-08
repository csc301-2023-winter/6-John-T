from django.db import models

class Park(models.Model):
    """
    Model representing a park.
    """
    park_id = models.AutoField(primary_key=True) #PK 
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)