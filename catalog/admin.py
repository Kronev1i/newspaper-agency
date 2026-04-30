from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Redactor, Topic, Newspaper


@admin.register(Redactor)
class RedactorAdmin(admin.ModelAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )

    admin.site.register(Newspaper)
    admin.site.register(Topic)