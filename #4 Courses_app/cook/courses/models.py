from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    preparation = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name='recipe',
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.title


class Branch(models.Model):
    latitude = models.CharField(max_length=100),
    longitude = models.CharField(max_length=100),
    address = models.CharField(max_length=100)
    course = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='branches'
        )


class Contact(models.Model):

    class Type(models.IntegerChoices):
        PHONE = 1,
        FACEBOOK = 2,
        EMAIL = 3

    type = models.IntegerField(choices=Type.choices)
    value = models.CharField(max_length=250)
    course = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return self.value
