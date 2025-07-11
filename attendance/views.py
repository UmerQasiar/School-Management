from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView
from rest_framework.exceptions import PermissionDenied
from .models import Attendance
from .serializers import AttendanceSerializer

class AttendanceListCreateAPIView(ListCreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        role = getattr(user.profile, 'role', None)

        if role == 'teacher' and hasattr(user, 'teacher'):
            student_ids = user.teacher.classes.values_list('students__id', flat=True)
            return Attendance.objects.filter(student__id__in=student_ids)
        elif role == 'student' and hasattr(user, 'student'):
            return Attendance.objects.filter(student=user.student)
        return Attendance.objects.none()

    def perform_create(self, serializer):
        user = self.request.user
        role = getattr(user.profile, 'role', None)

        if role != 'teacher' or not hasattr(user, 'teacher'):
            raise PermissionDenied("Only teachers can mark attendance.")

        student = serializer.validated_data['student']
        if not user.teacher.classes.filter(students=student).exists():
            raise PermissionDenied("You can only mark attendance for your own students.")

        serializer.save(teacher=user.teacher)
