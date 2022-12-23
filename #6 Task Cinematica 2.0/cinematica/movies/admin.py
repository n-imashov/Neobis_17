from django.contrib import admin
from .models import *

admin.site.register(Cinemas)
admin.site.register(Movie)
admin.site.register(RoomsFormat)
admin.site.register(Rooms)
admin.site.register(MovieFormat)
admin.site.register(ShowTime)

