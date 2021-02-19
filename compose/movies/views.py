# Standard Library
import math

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import FormView
from django.views.generic import ListView

# Local
from .forms import MovieFindForm
from .models import Movie
from .utils import create_movies
from .utils import create_url_params
from .utils import get_data_from_api


class MovieFinderFormView(LoginRequiredMixin, FormView):

    template_name = 'movies/search_form.html'
    form_class = MovieFindForm


def get_options(page_no, pages):
    if page_no == 1 and pages < 4:
        return [i for i in range(1, pages)]
    elif page_no == 1 and pages > 3:
        return [i for i in range(1, 4)]
    elif page_no == pages:
        return [i for i in range(pages+1)][-3:]
    else:
        return [page_no - 1, page_no, page_no + 1]


class MovieListView(LoginRequiredMixin, ListView):
    template_name = 'movies/list.html'

    def get_queryset(self):
        params, self.page_no = create_url_params(self.request)
        api_url = f'http://www.omdbapi.com/?{params}apikey=60110a3f'
        self.movies, self.results = get_data_from_api(api_url)
        return self.movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movies'] = self.movies
        context['results'] = self.results
        context['current_page'] = self.page_no
        if self.results:
            context['pages_no'] = math.ceil(int(self.results)/10)
            context['page_options'] = get_options(self.page_no, context['pages_no'])
            create_movies(self.movies)
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
