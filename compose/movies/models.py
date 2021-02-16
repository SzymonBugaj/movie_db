from django.db import models


class Movie(models.Model):

    name = models.CharField(
        'name',
        max_length=255,
    )
    release_date = models.DateField('Release date')
    box_office = models.PositiveIntegerField('Box office')
