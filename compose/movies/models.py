# Django
from django.db import models


class Movie(models.Model):

    title = models.CharField(
        'Title',
        max_length=255,
    )
    year_of_release = models.DateField(
        'Release date',
        blank=True,
        null=True,
    )
    box_office = models.PositiveIntegerField(
        'Box office',
        blank=True,
        null=True,
    )
