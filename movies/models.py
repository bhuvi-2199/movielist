from django.db import models
import json

class Movie(models.Model):

    title = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    year = models.IntegerField()

    def __str__(self):
        return json.dumps(self.to_dict())

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'director': self.director,
            'year': self.year
        }



class User(models.Model):

    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    my_movies = models.ManyToManyField(Movie)

    def __str__(self):
        return json.dumps(self.to_dict())

    def not_my_movies(self):
        result = []
        for movie in Movie.objects.all():
            if (movie not in self.my_movies.all()):
                result.append(movie)
        return result

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'username': self.username
        }


