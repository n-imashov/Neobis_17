from django.contrib import admin
from .models import *

admin.site.register([Cinemas, Movie, RoomsFormat, Rooms, MovieFormat, ShowTime])
