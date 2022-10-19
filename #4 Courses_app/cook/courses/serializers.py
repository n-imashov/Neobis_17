from rest_framework import serializers
from .models import Recipe, Contact, Branch


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ('title', 'category')

    def create(self, validate_data):
        print(validate_data)
        contacts = validate_data.pop('contacts')
        branches = validate_data.pop('branches')
        courses = Contact.objects.create(**validate_data)
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
