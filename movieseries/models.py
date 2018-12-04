from django.db import models
from taggit.managers import TaggableManager

# Create your models here.


class Categories(models.Model):

    name = models.TextField(max_length=50, primary_key=True)

    def __str__(self):
        return self.name


class Movie(models.Model):

    id = models.AutoField(
        primary_key=True
    )
    title = models.TextField(
        max_length=200,
        verbose_name='Title'
    )
    title_translated = models.TextField(
        max_length=200,
        blank=True,
        verbose_name='Translated Title'
    )
    director = models.TextField(
        max_length=150,
        blank=True,
        verbose_name='Director'
    )
    description = models.TextField(
        max_length=200,
        blank=True,
        verbose_name='Description'
    )
    added = models.DateField(
        auto_now_add=True,
        verbose_name='Added'
    )
    movie_year = models.PositiveSmallIntegerField(
        blank=True,
        verbose_name='Year'
    )
    cover = models.ImageField(
        upload_to='covers',
        blank=True,
        verbose_name='Cover',
        default="defaults/cover.png"

    )
    categories = models.ManyToManyField(
        Categories,
        blank=True,
        verbose_name='Categories'
    )
    trailer_link = models.TextField(
        blank=True
    )

    def __str__(self):
        return "{0}. {1}({2}) by {3}".format(self.id, self.title, self.movie_year, self.director)