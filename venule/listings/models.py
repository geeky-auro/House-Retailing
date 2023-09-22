from django.db import models
from datetime import datetime
from realtors.models import Realtors

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey(Realtors,on_delete=models.DO_NOTHING)
    title=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=20)
    # We pass true because we keep it as optional i.e if we dont add true then not adding description as a field of the table will arise error.
    description=models.CharField(blank=True)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2,decimal_places=1)
    garage=models.IntegerField(default=0)
    sqft=models.IntegerField()
    lot_size=models.DecimalField(max_digits=5,decimal_places=1)
    # The below Images should be uploaded to a folder 
    # Folder should have a specific format file <date-format> 
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    # There will be 6-different images that will be opened with the lightbox
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    is_published=models.BooleanField(default=True)
    list_date=models.DateTimeField(default=datetime.now,blank=True)
    def __str__(self):
        return self.title


