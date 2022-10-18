from django.forms import model_to_dict
from .models import Recipe
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import RecipeSerializer


class RecipeAPIView(APIView):
    def get(self, request):
        w = Recipe.objects.all()
        return Response({'posts': RecipeSerializer(w, many=True).data})

    def post(self, request):
        post_new = Recipe.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({'post': model_to_dict(post_new)})
