from django.contrib import admin

from .models import Category, Branch, Contact, Course


class ContactInline(admin.TabularInline):
    model = Contact
    extra = 3


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    inlines = [ContactInline]


admin.site.register(Category)
admin.site.register(Branch)
admin.site.register(Contact)
# admin.site.register(Course)
