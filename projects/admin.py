from django.contrib import admin
from projects.models import (Tag,
                             Task,
                             Project)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name", )

    list_display = ("name", "project__name", "status", "priority", "due_date", "created_at")

    list_filter = ("status", "priority", "project__name", "due_date", "created_at")


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ("name", )

    list_display = ("name", "created_at")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...
