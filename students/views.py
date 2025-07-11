from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentRegisterSerializer
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

