from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import BranchView, ContactViewSet, RecipeListView, CategoryView

router = DefaultRouter()
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('course/', CategoryView.as_view()),
    path('branch/', BranchView.as_view()),
    path('contact/', include(router.urls)),
    path('course-list/', RecipeListView.as_view()),
    path('course-create/', RecipeListView.as_view()),
    path('course/<int:pk>/', RecipeListView.as_view()),
]