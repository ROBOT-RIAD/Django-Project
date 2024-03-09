from django.db import models

# Create your models here.

class DjangoForm(models.Model):
    roll =models.IntegerField(primary_key=True)
    name =models.CharField(max_length=20)
    address =models.TextField()
    father_name=models.TextField(default=None)

    def __str__(self) -> str:
        return self.name