from django.db import models
from brand_name.models import CarModel
from django.contrib.auth.models import User
# Create your models here.
class Cars(models.Model):
    Car_name =models.CharField(max_length=200)
    description =models.TextField()
    quantity =models.IntegerField()
    price =models.IntegerField()
    brand_name =models.ForeignKey(CarModel,on_delete = models.CASCADE)
    coustomer =models.ForeignKey(User,on_delete = models.CASCADE,default=None,null=True,blank=True)
    image =models.ImageField(upload_to='Car/media/uploads/',blank=True,null=True)

    def __str__(self) -> str:
        return self.Car_name
    

class Comment(models.Model):
    post = models.ForeignKey(Cars,on_delete =models.CASCADE,related_name='comments')
    name = models.CharField(max_length =30)
    body =models.TextField()
    email =models.EmailField()
    created_on = models.DateTimeField(auto_now_add =True)
    
    def __str__(self) -> str:
        return f"comments by {self.name}"



