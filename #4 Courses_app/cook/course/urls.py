from django.urls import path, include
from rest_framework.routers import DefaultRouter
from course.views import CategoryView, BranchView, ContactViewSet, CourseListView, \
    CourseDetailView

router = DefaultRouter()
router.register(r'contact', ContactViewSet)

urlpatterns = [
    path('course/', CategoryView.as_view()),
    path('branch/', BranchView.as_view()),
    path('contact/', include(router.urls)),
    path('course-list/', CourseListView.as_view()),
    path('course-create/', CourseListView.as_view()),
    path('course/<int:pk>/', CourseDetailView.as_view()),
]

