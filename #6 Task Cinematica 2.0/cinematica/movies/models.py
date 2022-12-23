from django.db import models
from django.utils import timezone


class Cinemas(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    start = models.TimeField(auto_now_add=False)
    end = models.TimeField(auto_now_add=False)
    location = models.CharField(max_length=255)
    contacts = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    age_limit = models.IntegerField(blank=True, null=True)
    beginning_of_movie = models.DateField(auto_now=False, blank=True, null=True)
    ending_of_movie = models.DateField(auto_now=False, blank=True, null=True)

    def __str__(self):
        return self.name


class RoomsFormat(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Rooms(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    format = models.ForeignKey(RoomsFormat, on_delete=models.CASCADE)
    cinemas = models.ForeignKey(Cinemas, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MovieFormat(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class ShowTime(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(auto_now=False, blank=True, null=True)
    movie_format = models.ForeignKey(MovieFormat, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.start_time}"
