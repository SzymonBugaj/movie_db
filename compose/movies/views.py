# Django
import json
from pprint import pprint

import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView

from .forms import MovieFindForm
from .models import Movie
from accounts.models import CustomUser


class MovieFinderFormView(FormView):

    template_name = 'movies/search_form.html'
    form_class = MovieFindForm

    def form_valid(self, form):
        print('test')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(':O')
        return super().form_valid(form)


def create_url_params(request):
    movie_field_param_dict = {
        'title': 's',
        'year': 'y',
        'movie_kind': 'type'
    }
    params = ''
    for k, v in request.GET.items():
        if k in movie_field_param_dict.keys():
            params += f'{movie_field_param_dict[k]}={request.GET[k]}'
    return params


def get_data_from_api(api_url):
    """Get movies as dict."""
    response = requests.request(
        'GET',
        api_url
    )
    response_dict = json.loads(response.text)['Search']
    results_no = json.loads(response.text)['totalResults']
    for movie in response_dict:
        for param, value in movie.items():
            if value == 'N/A':
                movie[param] = None
    return response_dict, results_no


def create_movies(movies):
    movies_in_db = Movie.objects.all().values_list('imdb_id', flat=True)
    new_movies = []
    for movie in movies:
        print('test')
        if movie['imdbID'] not in movies_in_db:
            print('test')
            new_movies.append(Movie(
                title=movie['Title'],
                year=movie['Year'],
                kind=movie['Type'],
                imdb_id=movie['imdbID'],
                poster_url=movie['Poster'],
            ))
    Movie.objects.bulk_create(new_movies)


class MovieListView(TemplateView):

    template_name = 'movies/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        params = create_url_params(self.request)
        api_url = f'http://www.omdbapi.com/?{params}&apikey=60110a3f'
        movies, results = get_data_from_api(api_url)
        context['movies'] = movies
        context['results'] = results
        create_movies(movies)
        return context


def add_to_favourites(request):
    imdb_id = request.GET.get('movie_id')
    user = request.user
    movie = Movie.objects.get(imdb_id=imdb_id)
    result = False
    if movie not in user.favourite_movies.all():
        user.favourite_movies.add(movie)
        result = True
    return JsonResponse({'added': result})