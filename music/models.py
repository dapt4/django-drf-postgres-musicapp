from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=200)

class Album(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    year = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')

class Song(models.Model):
    title = models.CharField(max_length=200)
    duration = models.CharField(max_length=15)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    
    def __str__(self):
        return f'cancion: {self.title}'
