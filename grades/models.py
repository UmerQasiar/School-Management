from django.db import models
from assignments.models import Assignment
from students.models import Student

# Create your models here.
class Grade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    score = models.DecimalField(max_digits=5, decimal_places=2)
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.assignment.title}: {self.score}"
