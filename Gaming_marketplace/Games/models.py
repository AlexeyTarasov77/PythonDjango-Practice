from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    creator = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    