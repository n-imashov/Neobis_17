from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView

from .models import Recipe, Branch, Contact, Category
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RecipeSerializer, BranchSerializer, ContactSerializer, CategorySerializers


class RecipeListView(APIView):
    def get(self, request,  *args, **kwargs):
        course = Recipe.objects.all()
        serializer = RecipeSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


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
