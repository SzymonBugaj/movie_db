# Django
from django.urls import path

# Local
from .views import MovieFinderFormView, MovieListView, add_to_favourites

urlpatterns = [
    path('find_movies/', MovieFinderFormView.as_view(), name='find_movies'),
    path('movies_list/', MovieListView.as_view(), name='movies_list'),
    path('add_to_favourites/', add_to_favourites, name='add_to_favourites'),
]
