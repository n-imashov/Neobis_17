from django.urls import path

from .views import (
    CinemasView,
    CinemasDetailView,
    MovieView,
    MovieDetailView,
    ShowTimeView,
    ShowTimeDetailView,
    RoomsView,
    RoomsDetailView,
    RoomsFormatView,
    RoomsFormatDetailView,
    MovieFormatView,
    MovieFormatDetailView,
)


urlpatterns = [
    path("cinemas", CinemasView.as_view()),
    path('cinemas/<int:pk>', CinemasDetailView.as_view()),
    path('movies', MovieView.as_view()),
    path('movies/<int:pk>', MovieDetailView.as_view()),
    path('show-times', ShowTimeView.as_view()),
    path('show-times/<int:pk>', ShowTimeDetailView.as_view()),
    path('rooms', RoomsView.as_view()),
    path('rooms/<int:pk>', RoomsDetailView.as_view()),
    path('rooms-format', RoomsFormatView.as_view()),
    path('rooms-format/<int:pk>', RoomsFormatDetailView.as_view()),
    path('movies-format', MovieFormatView.as_view()),
    path('movies-format/<int:pk>', MovieFormatDetailView.as_view()),
]