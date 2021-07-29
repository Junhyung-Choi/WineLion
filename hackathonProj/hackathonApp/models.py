from django.db import models

# Create your models here.
class Wine(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    country = models.CharField( max_length=50)
    price = models.IntegerField()
    grape_type1= models.CharField(max_length=50)
    grape_type2= models.CharField(max_length=50)
    explain = models.CharField(max_length=200)
    taste1 = models.CharField(max_length=50)
    taste2 = models.CharField(max_length=50)
    alchol = models.FloatField()
    dry = models.FloatField()
    body = models.FloatField()
    tannin = models.FloatField()

class Review(models.Model):
    user_id = 1 #need to fill foreign key
    write_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    star = models.IntegerField()
    body = models.TextField()
    wine_id = 1 #need to fill foreign key

class Event(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = 2 #need to fill imagefield

