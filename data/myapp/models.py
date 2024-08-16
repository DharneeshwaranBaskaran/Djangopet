from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    url = models.URLField()
    weight = models.DecimalField(max_digits=5, decimal_places=2) 
    Category=models.CharField(max_length=100, default='Fish') 
    like =models.IntegerField(default=0)
    dislike=models.IntegerField(default=0)

class logincredentials(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100) 
    email = models.CharField(max_length=100, default='NO Email')
    
