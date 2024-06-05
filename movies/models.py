from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(default=True)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    summary = models.TextField()

    def __str__(self):
        return self.title

class apiMovies(models.Model):
    name = models.CharField(max_length=255,null=True)
    title = models.CharField(max_length=255)
    release_date = models.CharField(max_length=10, blank=True, null=True)
    release_month = models.CharField(max_length=2, blank=True, null=True)
    release_year = models.CharField(max_length=4, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    title_image_url = models.ImageField(default=True)

    def __str__(self):
        return self.title