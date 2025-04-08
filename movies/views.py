from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Movie, Genre
from .forms import MovieForm

# List View
class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'
    paginate_by = 12

# Detail View
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'

# Create View
class MovieCreateView(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie-list')

# Update View
class MovieUpdateView(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'movies/movie_form.html'
    success_url = reverse_lazy('movie-list')

# Delete View
class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie-list')

# Search View
def search_movies(request):
    query = request.GET.get('q', '')
    movies = Movie.objects.filter(title__icontains=query) if query else Movie.objects.none()
    return render(request, 'movies/search_results.html', {'movies': movies, 'query': query})

# Filter by Genre
def filter_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    movies = Movie.objects.filter(genres=genre)
    return render(request, 'movies/movie_list.html', {'movies': movies, 'genre': genre})

# Filter by Watched Status
def filter_by_watched(request, watched):
    watched_bool = (watched == 'watched')
    movies = Movie.objects.filter(watched=watched_bool)
    status = "Watched" if watched_bool else "Unwatched"
    return render(request, 'movies/movie_list.html', {'movies': movies, 'status': status})