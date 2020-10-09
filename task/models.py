from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ManyToManyField(User, blank=True, null=True)
    task_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.task_name

