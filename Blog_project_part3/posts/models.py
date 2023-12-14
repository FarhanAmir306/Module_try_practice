from django.db import models
from category.models import CatagoryModel
from django.contrib.auth.models import User
# Create your models here.
class PostModel(models.Model):
    title=models.CharField( max_length=100)
    content=models.TextField()
    category=models.ManyToManyField(CatagoryModel,)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='posts/media/uploads/',null=True,blank=True)
    
    def __str__(self):
        return self.title