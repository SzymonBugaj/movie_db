from django import forms

from movies.models import Movie


class MovieFindForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['title', ]
