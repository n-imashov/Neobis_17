from django.urls import path

from applications.category.views import CategoryListView

urlpatterns = [
    path('list/', CategoryListView.as_view())
]
