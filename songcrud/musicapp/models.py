from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=300) 
    last_name = models.CharField(max_length=300)  
    age = models.IntegerField() 

class Song(models.Model):
    pass

class Lyric(models.Model):
    pass