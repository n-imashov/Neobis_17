from django.contrib import admin

from .models import Recipe, Branch, Contact, Category


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 3


@admin.register(Recipe)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ContactInline]


admin.site.register(Branch)
admin.site.register(Contact)
admin.site.register(Category)
