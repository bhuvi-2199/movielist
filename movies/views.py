from django.shortcuts import render

from django.http import HttpResponse
from .models import Movie, User

from django.views.decorators.csrf import csrf_protect, csrf_exempt

import json 

def all_movies(request):

    if (request.method == 'GET'):

        movies = [movie.to_dict() for movie in Movie.objects.all()]
        return HttpResponse(json.dumps(movies),content_type='application/json')

def all_users(request):

    if (request.method == 'GET'):

        users = [user.to_dict() for user in User.objects.all()]
        return HttpResponse(json.dumps(users),content_type='application/json')


def movies_for_username(request):

    if (request.method == 'GET'):

        username = request.GET.get('username')

        user = User.objects.get(username=username)

        movies = [movie.to_dict() for movie in user.my_movies.all()]

        return HttpResponse(json.dumps(movies),content_type='application/json')

def add_movie_for_user(request):

    if (request.method == 'GET'):

        username = request.GET.get('username')
        password = request.GET.get('password')
        movie_id = request.GET.get('movie_id')

        try:
            user = User.objects.get(username=username,password=password)
        except:
            response = {
                'message': 'Invalid username or password'
            }
            return HttpResponse(json.dumps(response),content_type='application/json')

        try: 
            movie = Movie.objects.get(id=movie_id)
        except:
            response = {
                'message': 'Movie with given id does not exist'
            }
            return HttpResponse(json.dumps(response),content_type='application/json')

        try:
            existing_movie = user.my_movies.get(id=movie_id)
        except:
            existing_movie = None 

        if (existing_movie != None):
            response = {
                'message': 'Movie with given id already added for the given user'
            }
            return HttpResponse(json.dumps(response),content_type='application/json')
        
        user.my_movies.add(movie)
        response = {
            'message': 'Successfully added movie for user'
        }
        return HttpResponse(json.dumps(response),content_type='application/json')
        

        