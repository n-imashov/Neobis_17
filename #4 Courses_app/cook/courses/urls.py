from django.urls import path, include
from rest_framework.routers import DefaultRouter
from courses.views import BranchView, ContactViewSet, RecipeAPIView

router = DefaultRouter()
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('recipe/', RecipeAPIView.as_view()),
    path('branch/', BranchView.as_view()),
    path('contact/', include(router.urls)),
]