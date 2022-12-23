import datetime
import pytz
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import (
    Cinemas,
    Movie,
    ShowTime,
    Rooms,
    RoomsFormat,
    MovieFormat,
)

utc = pytz.UTC


class CinemasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinemas
        fields = ('id', 'name', 'start', 'end', 'location', 'contacts')


class MovieFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFormat
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):

    movie_status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = [
            'id',
            'name',
            'age_limit',
            'beginning_of_movie',
            'ending_of_movie',
            'movie_status',
        ]

    @staticmethod
    def get_movie_status(obj):

        now = datetime.date.today()

        if obj.beginning_of_movie <= now <= obj.ending_of_movie:
            obj.movie_status = 'current'
            return obj.movie_status

        if obj.beginning_of_movie > now:
            obj.movie_status = 'upcoming'
            return obj.movie_status


class ShowTimeSerializer(serializers.ModelSerializer):

    is_active = serializers.SerializerMethodField()

    class Meta:
        model = ShowTime
        fields = [
            'id',
            'start_time',
            'end_time',
            'movie_format',
            'movie',
            'rooms',
            'is_active',
        ]

    @staticmethod
    def get_is_active(obj):
        end_time = obj.end_time.replace(tzinfo=utc)
        a = datetime.datetime.now()
        now = a.replace(tzinfo=utc)
        if now > end_time:
            obj.is_active = False
            obj.save()
        return obj.is_active


class RoomsFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomsFormat
        fields = [
            'id',
            'name',
            'price',
        ]


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = [
            'id',
            'name',
            'format',
            'cinemas',
        ]