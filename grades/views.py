# grades/views.py

from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.exceptions import PermissionDenied
from .models import Grade
from .serializers import GradeSerializer
from users.models import Profile

class GradeListCreateAPIView(ListCreateAPIView):
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        role = getattr(user.profile, 'role', None)

        if role == 'teacher' and hasattr(user, 'teacher'):
            student_ids = user.teacher.classes.values_list('students__id', flat=True)
            return Grade.objects.filter(student__id__in=student_ids)
        elif role == 'student' and hasattr(user, 'student'):
            return Grade.objects.filter(student=user.student)
        return Grade.objects.none()

    def perform_create(self, serializer):
        role = getattr(self.request.user.profile, 'role', None)
        if role != 'teacher':
            raise PermissionDenied("Only teachers can create grades.")
        serializer.save()
