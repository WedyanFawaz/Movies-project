from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Movie(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    
    title = models.CharField(max_length=200)
    director = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    poster = models.ImageField(upload_to='movie_posters/', blank=True, null=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=3)
    watched = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} ({self.release_year})"
    
    def get_absolute_url(self):
        return reverse('movie-detail', args=[str(self.id)])
        
    class Meta:
        ordering = ['-date_added']