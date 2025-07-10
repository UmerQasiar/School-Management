from django.db import models
from teachers.models import Teacher
from students.models import Student

# Create your models here.
class Class(models.Model):
    section = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name='classes')
    students = models.ManyToManyField(Student, related_name='classes')

    def __str__(self):
        return f"{self.section} - {self.section}"
