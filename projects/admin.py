"""Задание 4 Артём
Настройте отображение моделей Project, Task, Tag в админ-панели. Реализуйте следующие возможности:
Поиск по названию задачи для модели Task.
Поиск по названию проекта для модели Project.
У модели Task в Админ-панели должны отображаться поля:
Название задачи
Проект
Статус
Приоритетность
Дата созданияДата сдачи задачи (due_date)"""

from django.contrib import admin
from projects.models import (Tag,
                             Task,
                             Project)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_display = ("name", "project_name", "status", "priority", "due_date", "created_at")
    list_filter = ("status", "priority", "project_name", "due_date", "created_at")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_display = ("name", "created_at")

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...

