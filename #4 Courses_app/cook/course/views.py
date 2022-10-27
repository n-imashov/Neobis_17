from rest_framework import status, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Category, Branch, Contact, Course
from course.serializers import CategorySerializers, BranchSerializer, ContactSerializer, CourseSerializer


class CategoryView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BranchView(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class CourseListView(APIView):
    def get(self, request,  *args, **kwargs):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CourseDetailView(APIView):
    def get_object(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise KeyError('ТААА-ШАААААA')

    def get(self, request, pk):
        course = self.get_object(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(f'"{course}" course was deleted!')

