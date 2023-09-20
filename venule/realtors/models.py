from django.db import models
from datetime import datetime

class Realtors(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description=models.TextField(blank=True)
    phone=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    is_mvp=models.BooleanField(default=False)
    hire_date=models.DateTimeField(default=datetime.now,blank=True)
    ## just like Listings we need to have a main field which needs to be displayed 
    def __str__(self) -> str:
        return self.name