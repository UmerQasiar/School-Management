from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsAdminUserRole  # 👈 Your custom admin role check
from .models import Subject
from .serializers import SubjectSerializer

class SubjectListCreateAPIView(ListCreateAPIView):
    serializer_class = SubjectSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated(), IsAdminUserRole()]
        return [IsAuthenticated()]

    def get_queryset(self):
        return Subject.objects.all()
