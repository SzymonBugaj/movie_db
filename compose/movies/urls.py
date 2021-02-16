# Django
from django.urls import path

# Local
from .views import MovieFinderFormView, get_movies_from_api

urlpatterns = [
    path('find_movies/', MovieFinderFormView.as_view(), name='find_movies'),
    path('get_movies_from_api/', get_movies_from_api, name='get_movies_from_api'),
]
