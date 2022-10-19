from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    serves = models.CharField(max_length=50)
    prep_time = models.PositiveIntegerField(default=0)
    cook_time = models.PositiveIntegerField(default=0)
    ingredients = models.TextField()
    preparation = models.TextField()
    category = models.ForeignKey(
        'Category',
        related_name='recipe',
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return self.title


class Branch(models.Model):
    latitude = models.CharField(max_length=100),
    longitude = models.CharField(max_length=100),
    address = models.CharField(max_length=100)


class Contact(models.Model):
    type = models.IntegerField(),
    email = models.EmailField()
    value = models.CharField(max_length=100)


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
