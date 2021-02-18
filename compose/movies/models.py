# Django
from django.db import models


class Movie(models.Model):

    title = models.CharField(
        'Title',
        max_length=255,
    )
    year = models.CharField(
        'Release date',
        blank=True,
        null=True,
        max_length=9,
    )
    imdb_id = models.CharField(
        'IMDB id',
        blank=True,
        null=True,
        max_length=20,
    )
    kind = models.CharField(
        'Type',
        blank=True,
        null=True,
        max_length=50,
    )
    poster_url = models.URLField(
        'Poster url',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.title
