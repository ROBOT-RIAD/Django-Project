from django.db import models
from musician.models import MusicianModel

# Create your models here.

class AlbumModel(models.Model):
    album_name=models.CharField(max_length=100)
    release_date =models.DateTimeField()
    rating=models.CharField(max_length=1)
    musician=models.ForeignKey(MusicianModel,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.album_name
