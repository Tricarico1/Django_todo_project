from django.db import models # type: ignore

# Create your models here.
class Todo(models.Model):
    content = models.TextField()