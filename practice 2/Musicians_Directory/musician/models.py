from django.db import models

# Create your models here.

class MusicianModel(models.Model):
    first_name =models.CharField(max_length=50)
    last_name =models.CharField(max_length=50)
    email =models.EmailField()
    phone_no=models.CharField(max_length=11)
    Instrument_Type=models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.last_name

