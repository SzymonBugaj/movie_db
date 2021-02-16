from django.contrib.auth.models import AbstractUser
from django.db import models

from movies.models import Movie


class CustomUser(AbstractUser):

    last_visit = models.DateTimeField('Last visit')
    favourite_movies = models.ManyToManyField(
        Movie,
        verbose_name='Favourite movies',
    )

    class Meta:  # noqa: D106

        verbose_name = 'User'
        verbose_name_plural = 'Users'
