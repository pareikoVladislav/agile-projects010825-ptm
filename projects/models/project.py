from django.db import models


#from projects import models


class Project(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    created_at = models.DateField(
        auto_now_add=True # параметр
    )


"""1 Задание: Создайте модель Project со следующими полями:

Название проекта: строковое поле, уникальное
Описание проекта: строковое поле, большое поле, обязательное
Дата создания проекта: должно автоматически устанавливаться при создании"""