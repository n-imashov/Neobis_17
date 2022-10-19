from rest_framework import serializers
from .models import Recipe, Contact, Branch, Category


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'name'


class BranchSerializer(serializers.ModelSerializer):
    course = serializers.Serializer(required=False)

    class Meta:
        model = Branch
        fields = ('longitude', 'address')


class ContactSerializer(serializers.ModelSerializer):
    course = serializers.Serializer(required=False)

    class Meta:
        model = Contact
        fields = ('id', 'email')


class RecipeSerializer(serializers.ModelSerializer):
    contacts = ContactSerializer(many=True)
    branches = BranchSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('title', 'category')

    def create(self, validate_data):
        print(validate_data)
        contacts = validate_data.pop('contacts')
        branches = validate_data.pop('branches')
        courses = Recipe.objects.create(**validate_data)
        for contact in contacts:
            Contact.objects.create(type=contact.get('type', ''),
                                   courses=courses,
                                   value=contact.get('value', '')
                                   )

        for branch in branches:
            Branch.objects.create(
                courses=courses,
                longitude=branch.get('longitude', ''),
                latitude=branch.get('latitude', ''),
                address=branch.get('address', '')
            )

        return courses