from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminOrTeacherUserRole
from .models import Assignment
from .serializers import AssignmentSerializer


class AssignmentListCreateAPIView(ListCreateAPIView):
    serializer_class = AssignmentSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminOrTeacherUserRole()]
        return [IsAuthenticated()]

    def get_queryset(self):
        user = self.request.user
        role = getattr(user.profile, 'role', None)

        if role in ['admin', 'staff']:
            return Assignment.objects.all()
        elif role == 'teacher' and hasattr(user, 'teacher'):
            return Assignment.objects.filter(teacher=user.teacher)
        elif role == 'student' and hasattr(user, 'student'):
            return Assignment.objects.filter(class_assigned__in=user.student.classes.all())
        return Assignment.objects.none()

class AssignmentDetailAPIView(RetrieveAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'

