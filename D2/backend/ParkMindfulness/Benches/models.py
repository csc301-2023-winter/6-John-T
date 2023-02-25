from django.db import models

# Here would go the bench model to be created by Sam
class Park(models.Model):
    park_id = models.AutoField(primary_key=True) #PK 
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

class Benches(models.Model):
    bench_id = models.AutoField(primary_key=True) #PK 
    bench_title = models.CharField(max_length=30)
    park_id = models.ForeignKey(Park, on_delete=models.CASCADE) #FK 
    #images 
    qr_code = models.ImageField(null=True, blank=True, upload_to="images/")
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images/")
