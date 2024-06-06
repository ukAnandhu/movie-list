from django.db import models

class Movies(models.Model):
    genre = models.CharField(max_length=255,null=True)
    title = models.CharField(max_length=255)
    summary = models.TextField(blank=True)
    release_year = models.CharField(max_length=4, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    title_image_url = models.URLField(max_length=500, null=True, blank=True)
    title_image = models.ImageField(upload_to='movies/', null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_image_url(self):
        if self.title_image:
            return self.title_image.url
        return self.title_image_url