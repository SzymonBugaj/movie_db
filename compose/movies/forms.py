# Django
from django import forms

# Project
from movies.models import Movie


class MovieFindForm(forms.ModelForm):

    title = forms.CharField(
        label='title',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mr-sm-2',
                'placeholder': 'title',
            }),
    )
    year = forms.CharField(
        label='year',
        required=False,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control mr-sm-2',
                'placeholder': 'year',
            }),
    )

    class Meta:
        model = Movie
        fields = ['title', 'year']
