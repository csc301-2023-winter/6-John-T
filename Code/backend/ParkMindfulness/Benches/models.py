from django.db import models
from Parks.models import Park

class Benches(models.Model):
    """
    Model class for Benches.
    """

    bench_id = models.AutoField(primary_key=True) #PK 
    bench_title = models.CharField(max_length=30)
    park_id = models.ForeignKey(Park, on_delete=models.CASCADE) #FK 
    #images 
    qr_code = models.ImageField(null=True, blank=True, upload_to="images/qr_codes/")
    thumbnail = models.ImageField(null=True, blank=True, upload_to="images/bench_thumbnails/")

class Audio(models.Model):
    """
    Model representing an audio file that is associated with a bench.

    The audio_binary describes if the audio exists and is False by default.
    The audio_file, contributor, length_category, and season_category are
    all optional fields.
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
        """
        Returns the length category for the Audio model.
        """
        return Audio.Length_Category(self.length_category)
    
    def get_season_category(self): 
        """
        Returns the season category for the Audio model.
        """
        return Audio.Season_Category(self.season_category)
    