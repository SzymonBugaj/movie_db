# Django
import requests
from django.views.generic import FormView

from .forms import MovieFindForm


class MovieFinderFormView(FormView):

    template_name = 'movies/movies.html'
    form_class = MovieFindForm

    def form_valid(self, form):
        print('test')
        return super().form_valid(form)

    def form_invalid(self, form):
        print(':O')
        return super().form_valid(form)


def get_movies_from_api(request):
    print('test', request.POST)
    movie_field_param_dict = {
        'title': 't',
        'year_of_release': 'y',
    }

    api_url = 'http://www.omdbapi.com/?t=batman&apikey=60110a3f'
    response = requests.request(
        'GET',
        api_url
    )
    print('response', response)
    return