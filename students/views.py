from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentRegisterSerializer, StudentSerializer
from users.permissions import IsAdminUserRole

class StudentRegisterAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserRole]

    def post(self, request):
        serializer = StudentRegisterSerializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            return Response({
                "message": "Student registered successfully",
                "student_id": student.id,
                "username": student.user.username,
                "email": student.user.email,
                "enrollment_number": student.enrollment_number,
                "class_ids": [c.id for c in student.classes.all()]
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentListAPIView(ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        role = getattr(user.profile, 'role', None)

        if role == 'admin':
            return Student.objects.all()
        elif role == 'teacher' and hasattr(user, 'teacher'):
            return Student.objects.filter(classes__teacher=user.teacher).distinct()
        elif role == 'student' and hasattr(user, 'student'):
            return Student.objects.filter(id=user.student.id)
        return Student.objects.none()
