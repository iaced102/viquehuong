from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Category(models.Model):
    type = models.CharField(max_length=20)
    def __str__(self):
        return self.type




class Description_image(models.Model):
    image = models.ImageField(upload_to='static/image/products', default = 'static/image/products/default.png')

    

class Product(models.Model):
    name                = models.CharField(max_length=50)
    price               = models.CharField(max_length=30)
    description         = models.TextField()
    sold                = models.PositiveIntegerField(default=0)
    count_vote          = models.PositiveIntegerField(default=0)
    vote                = models.PositiveIntegerField(default=0)
    description_image   = models.ManyToManyField(Description_image, blank=True)
    def __str__(self):
        return self.name



class Comment_and_Vote(models.Model):
    comment     = models.TextField()
    vote        = models.PositiveIntegerField(blank=True)
    post        = models.ForeignKey(Product, on_delete=models.CASCADE)
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.post