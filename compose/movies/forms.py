from django import forms

from compose.movies.models import Movie


class MovieFindForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', ]
