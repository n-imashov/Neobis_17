import datetime
from rest_framework import generics
from .serializers import (
    CinemasSerializer,
    MovieSerializer,
    ShowTimeSerializer,
    RoomsSerializer,
    RoomsFormatSerializer,
    MovieFormatSerializer
)
from .models import (
    Cinemas,
    Movie,
    ShowTime,
    Rooms,
    RoomsFormat,
    MovieFormat,
)
from users.permissions import IsAdminOrReadOnly


class CinemasView(generics.ListCreateAPIView):
    serializer_class = CinemasSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Cinemas.objects.all()


class CinemasDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CinemasSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Cinemas.objects.all()


class MovieView(generics.ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.filter(ending_of_movie__gt=datetime.datetime.now())


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Movie.objects.all()


class ShowTimeView(generics.ListCreateAPIView):
    serializer_class = ShowTimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = ShowTime.objects.filter(is_active=True)


class ShowTimeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ShowTimeSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = ShowTime.objects.all()


class RoomsView(generics.ListCreateAPIView):
    serializer_class = RoomsSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Rooms.objects.all()


class RoomsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomsSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = Rooms.objects.all()


class RoomsFormatView(generics.ListCreateAPIView):
    serializer_class = RoomsFormatSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = RoomsFormat.objects.all()


class RoomsFormatDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomsFormatSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = RoomsFormat.objects.all()


class MovieFormatView(generics.ListCreateAPIView):
    serializer_class = MovieFormatSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = MovieFormat.objects.all()


class MovieFormatDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieFormatSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    queryset = MovieFormat.objects.all()
