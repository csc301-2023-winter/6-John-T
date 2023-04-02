from django.db import models
from Parks.models import Park

class Benches(models.Model):
    bench_id = models.AutoField(primary_key=True) #PK 
    bench_title = models.CharField(max_length=30)
    park_id = models.ForeignKey(Park, on_delete=models.CASCADE) #FK 
    #images 
    qr_code = models.ImageField(null=True, blank=True, upload_to="images/qr_codes/")
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images/bench_thumbnails/")

# Audio Model
# Length_Category: The 1st value is the actual value and 
# the 2nd value is displayed on Django Admin
# https://stackoverflow.com/questions/18676156/how-to-properly-use-the-choices-field-option-in-django
# Season_Category
# bench_id: related_name = 'audios' allows for reverse relationship (get all audios related to one bench)
# audio_binary: whether audio exists (True) or not (False)
# audio_file: store under 'media/audio_files/'
# length_category: 0-5, 5-10, >10 # TODO clarify categories with others 
# season_category: spring, summer, fall, winter 

class Audio(models.Model):
    """
    Model representing an audio file that is associated with a bench.
    """
    class Length_Category(models.TextChoices):
        SHORT = "0-5", "0-5 minutes"
        MEDIUM = "5-10", "5-10 minutes"
        LONG = ">10", "greater than 10 minutes"

    class Season_Category(models.TextChoices):
        SPRING = 'SP', 'Spring'
        SUMMER = 'SU', 'Summer'
        FALL = 'FA', 'Fall'
        WINTER = 'WI', 'Winter'

    audio_id = models.AutoField(primary_key=True) #PK 
    bench_id = models.ForeignKey(Benches, on_delete=models.CASCADE, related_name='audios') #FK
    audio_binary = models.BooleanField(default=False) 
    audio_file = models.FileField(upload_to='audio_files/', blank=True, null=True) #optional
    contributor = models.CharField(max_length=100, blank=True, null=True) #optional 
    length_category = models.CharField(max_length=30, 
                                       choices=Length_Category.choices,
                                       blank=True, 
                                       null=True) #optional 
    season_category = models.CharField(max_length=30, 
                                       choices=Season_Category.choices,
                                       blank=True, 
                                       null=True) #optional 
    
    def get_length_category(self): 
        return Audio.Length_Category(self.length_category)
    
    def get_season_category(self): 
        return Audio.Season_Category(self.season_category)
    