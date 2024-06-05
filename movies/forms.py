from django import forms
from .models import Movie, apiMovies

class MovieForm(forms.ModelForm):
    class Meta:
        model = apiMovies
        fields = ['title','name','title_image_url']
        