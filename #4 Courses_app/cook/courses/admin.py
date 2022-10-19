from django.contrib import admin

from .models import Recipe, Branch, Contact

admin.site.register(Recipe)
admin.site.register(Branch)
admin.site.register(Contact)
