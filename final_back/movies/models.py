from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    poster_path = models.CharField(max_length=200)
    overview = models.TextField()
    vote_average = models.FloatField()
    original_title = models.CharField(max_length=100)
    original_language = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    popularity = models.FloatField()
    homepage = models.CharField(max_length=200)
    revenue = models.IntegerField()
    runtime = models.IntegerField()
    budget = models.IntegerField()
    youtube_key = models.TextField()
    genres = models.ManyToManyField(Genre, related_name="movies_in_genre")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    
    def __str__(self):
        return self.title
    
class Actor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    popularity = models.FloatField()
    known_for_department = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200)
    acting_movies = models.ManyToManyField(Movie, related_name='actors_in_movie')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_actors')
    
    def __str__(self):
        return self.name

class Director(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    popularity = models.FloatField()
    known_for_department = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=200)
    directing_movies = models.ManyToManyField(Movie, related_name='director_in_movie')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_directors')

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rank = models.FloatField()
    
    def __str__(self):
        return self.content