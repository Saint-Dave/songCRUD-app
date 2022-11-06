from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)  
    age = models.IntegerField() 

class Song(models.Model):
    title = models.CharField() 
    date_released = models.DateField() 
    likes = models.ExpressionList
    artiste_id = models.CharField()


class Lyric(models.Model):
    content = models.CharField()
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)