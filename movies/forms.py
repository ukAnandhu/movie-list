from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['title','genre','rating','title_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'genre': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control custom-input'}),
            'title_image': forms.ClearableFileInput(attrs={'class': 'form-control custom-input'}),
        }
        