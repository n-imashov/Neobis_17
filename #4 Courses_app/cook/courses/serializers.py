from rest_framework import serializers

from courses.models import Category, Branch, Contact, Recipe


class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    course = serializers.Serializer(required=False)

    class Meta:
        model = Branch
        fields = ('id', 'longitude', 'latitude', 'address', 'course', )


class ContactSerializer(serializers.ModelSerializer):
    course = serializers.Serializer(required=False)

    class Meta:
        model = Contact
        fields = ('id', 'type', 'value', 'course', )


class RecipeSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ['title', 'category']

    def create(self, validate_data):
        print(validate_data)
        contacts = validate_data.pop('contacts')
        branches = validate_data.pop('branches')

        course = Recipe.objects.create(**validate_data)
        for contact in contacts:
            Contact.objects.create(type=contact.get('type', ''), course=course, value=contact.get('value', ''))

        for branch in branches:
            Branch.objects.create(
                course=course, longitude=branch.get('longitude', ''),
                latitude=branch.get('latitude', ''), address=branch.get('address', '')
            )

        return course
