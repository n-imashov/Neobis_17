from django.contrib import admin
from django.urls import path, include

from movies.views import CinemasView
from users.views import RegisterView


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/v1/Cinemaslist/', CinemasView.as_view()),
    path('user/', include('users.urls')),
    path('movies/', include('movies.urls')),
    path('purchase/', include('tickets.urls')),
    path('', RegisterView.as_view()),
]
