
from django.contrib import admin
from django.urls import path

from courses.views import RecipeListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/recipelist/', RecipeListView.as_view())
]
