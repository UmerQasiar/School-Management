from django.db import models
from classes.models import Class

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)
    class_assigned = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subjects')


    def __str__(self):
        return f"{self.name} ({self.class_assigned})"
