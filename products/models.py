from django.db import models
from django.utils import timezone
from base.models import User


class Category(models.Model):
    c_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.c_name


class Products(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    f_image1 = models.ImageField(upload_to='products/')
    f_image2 = models.ImageField(upload_to='products/')
    f_image3 = models.ImageField(upload_to='products/')
    categories = models.ManyToManyField(Category)
    state = models.BooleanField()

    def __str__(self):
        return self.name
