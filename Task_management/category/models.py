from django.db import models
from task.models import TaskModel

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)
    tasks = models.ManyToManyField(TaskModel)

    def __str__(self):
        return self.name
