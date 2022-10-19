from rest_framework import viewsets, generics, status
from .models import Recipe, Branch, Contact
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RecipeSerializer, BranchSerializer, ContactSerializer, CategorySerializers


class RecipeAPIView(APIView):
    def get(self, request):
        category = Recipe.objects.all()
        serializer = RecipeSerializer(category, many=True)
        return Response({'posts': RecipeSerializer(category, many=True).data})


class BranchView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


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
