from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Movie, Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_year', 'rating', 'watched', 'date_added')
    list_filter = ('genres', 'watched', 'rating', 'release_year')
    search_fields = ('title', 'director', 'notes')
    readonly_fields = ('date_added',)
    filter_horizontal = ('genres',)