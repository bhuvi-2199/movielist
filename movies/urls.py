from django.urls import path 
from . import views 

urlpatterns = [
    path('all-movies/', views.all_movies, name='all_movies'),
    path('movies-for-username/', views.movies_for_username, name='movies_for_username'),
    path('all-users/', views.all_users, name='all_users'),
    path('add-movie-for-user', views.add_movie_for_user, name='add_movie_for_user')
]