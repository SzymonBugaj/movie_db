import json
import requests
from .models import Movie


def create_url_params(request):
    movie_field_param_dict = {
        'title': 's',
        'year': 'y',
        'movie_kind': 'type',
        'page': 'page'
    }
    params = ''
    for k, v in request.GET.items():
        if k in movie_field_param_dict.keys() and request.GET[k]:
            params += f'{movie_field_param_dict[k]}={request.GET[k]}&'
    if not 'page' in request.GET:
        page_no = 1
    else:
        page_no = request.GET['page']
    return params, int(page_no)


def get_data_from_api(api_url):
    """Get movies as dict."""
    response = requests.request(
        'GET',
        api_url
    )
    if 'Error' in json.loads(response.text):
        return json.loads(response.text)['Error'], None
    response_dict = json.loads(response.text)['Search']
    results_no = json.loads(response.text)['totalResults']
    for movie in response_dict:
        for param, value in movie.items():
            if value == 'N/A':
                movie[param] = None
    return response_dict, results_no


def create_movies(movies):
    """Add movies to db."""
    movies_in_db = Movie.objects.all().values_list('imdb_id', flat=True)
    new_movies = []
    for movie in movies:
        if movie['imdbID'] not in movies_in_db:
            new_movies.append(Movie(
                title=movie['Title'],
                year=movie['Year'],
                kind=movie['Type'],
                imdb_id=movie['imdbID'],
                poster_url=movie['Poster'],
            ))
    Movie.objects.bulk_create(new_movies)