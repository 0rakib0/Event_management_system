from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to='artist_pic')
    date_of_birth = models.DateField()
    music_type = models.CharField(max_length=120)
    youtube_channel = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self) -> str:
        return self.name
    
    @staticmethod
    def get_artist_list():
        return Artist.objects.all()
        