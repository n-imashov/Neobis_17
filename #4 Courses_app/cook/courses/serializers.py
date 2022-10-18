from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Recipe



class RecipeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    serves = serializers.CharField(max_length=50)
    prep_time = serializers.IntegerField(default=0)
    cook_time = serializers.IntegerField(default=0)
    ingredients = serializers.CharField()
    preparation = serializers.CharField()
    category = serializers.ImageField()






#class RecipeModel:
#    def __int__(self, title, content):
#        self.title = title
#        self.content = content
#


#def encode():
#    model = RecipeModel()
#    model_sr = RecipeSerializer(model)
#    print(model_sr.data, type(model_sr.data), sep='\n')
#    json = JSONRenderer().render(model_sr.data)
#    print(json)
#
#
#def decode():
#    stream = io.BytesIO()