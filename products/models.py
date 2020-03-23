from django.db import models

class Product(models.Model):
    brand = models.CharField(max_length=200,null=True,blank=True)
    name = models.CharField(max_length=254, default='')
    price = models.CharField(max_length=255)
    rating = models.CharField(max_length=40,default=0.0)
    image = models.CharField(max_length=200,null=True,blank=True)
    #image = models.ImageField(max_length=1000, upload_to='images')
    url = models.CharField(max_length=200,null=True,blank=True)
    seller = models.CharField(max_length=200,default="AllinOne")

    def __str__(self):
        return str(self.name)