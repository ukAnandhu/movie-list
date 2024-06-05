from django.contrib import admin

# Register your models here.
from .models import Movie,apiMovies

admin.site.register(Movie)
admin.site.register(apiMovies)
