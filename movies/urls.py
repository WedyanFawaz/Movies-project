from django.urls import path
from . import views

urlpatterns = [
    path('', views.MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movie/new/', views.MovieCreateView.as_view(), name='movie-create'),
    path('movie/<int:pk>/edit/', views.MovieUpdateView.as_view(), name='movie-update'),
    path('movie/<int:pk>/delete/', views.MovieDeleteView.as_view(), name='movie-delete'),
    path('search/', views.search_movies, name='movie-search'),
    path('genre/<int:genre_id>/', views.filter_by_genre, name='genre-filter'),
    path('status/<str:watched>/', views.filter_by_watched, name='watched-filter'),
]