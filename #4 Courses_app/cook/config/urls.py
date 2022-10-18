
from django.contrib import admin
from django.urls import path

from courses.views import RecipeAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/recipelist/', RecipeAPIView.as_view())
]
