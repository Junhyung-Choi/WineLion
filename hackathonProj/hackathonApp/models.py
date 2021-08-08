from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.
class Wine(models.Model):
    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)
    country = models.CharField( max_length=50)
    price = models.IntegerField()
    grape_type1= models.CharField(max_length=50)
    grape_type2= models.CharField(max_length=50, null = True)
    explain = models.CharField(max_length=200)
    taste1 = models.CharField(max_length=50)
    taste2 = models.CharField(max_length=50)
    alchol = models.FloatField()
    dry = models.FloatField()
    body = models.FloatField()
    tannin = models.FloatField()
    

    def __str__(self):
        return self.name

class Review(models.Model):
    referring_user_id = models.ForeignKey("hackathonApp.CustomUser", on_delete=models.CASCADE)
    write_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    last_modified_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    star = models.IntegerField()
    body = models.TextField()
    referring_wine_id = models.ForeignKey("hackathonApp.Wine", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.referring_user_id)

class Event(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    image = models.ImageField(upload_to='images/',blank = True, null = True)
    wines = models.ManyToManyField("hackathonApp.Wine")

    def __str__(self):
        return self.title


class CustomUser(AbstractUser):
    USER_GRADE = (
        ('S','Silver'),
        ('G','Gold'),
        ('V','VIP'),
    )
    Gender = (
        ('F','Female'),
        ('M','Male'),
    )
    grade = models.CharField("유저등급", max_length=10, choices=USER_GRADE, default='S')
    register_date = models.DateTimeField("가입일시",auto_now_add=True)
    birth = models.DateField("생년월일", null=True, blank=True)
    gender = models.CharField("성별", max_length=10, choices=Gender, default='F')


class Food(models.Model):
    name = models.CharField( max_length=50)
    FOOD_LOCATIONS = (
        ('KO','한식'),
        ('CH','중식'),
        ('JA','일식'),
        ('WE','양식'),
        ('DE','디저트'),
        ('WR','기타음식'),
    )
    location = models.CharField(max_length=10,choices=FOOD_LOCATIONS)
    tag1 = models.CharField(max_length=10)
    tag2 = models.CharField(max_length=10)
    wines = models.ManyToManyField("hackathonApp.Wine") 

    def __str__(self):
        return self.name