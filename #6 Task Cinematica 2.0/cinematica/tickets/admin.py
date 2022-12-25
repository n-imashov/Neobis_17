from django.contrib import admin
from .models import *

admin.site.register([Seats, Tickets, Orders, Feedback, Booking, ClubCard])