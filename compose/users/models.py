# Django
from django.contrib.auth.models import AbstractUser
from django.db import models

# 3rd-party


class CustomUser(AbstractUser):

    last_visit = models.DateTimeField(
        'Last visit',
        blank=True,
        null=True,
    )

    favourite_movies = models.ManyToManyField(
        'movies.Movie',
        verbose_name='Favourite movies',
    )

    class Meta:  # noqa: D106

        verbose_name = 'User'
        verbose_name_plural = 'Users'
