from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)  
    age = models.IntegerField() 

class Song(models.Model):
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)
    title = models.CharField(max_length=300) 
    date_released = models.DateField(default=datetime.today) 
    likes = models.IntegerField()

class Lyric(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)