from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from teachers.models import Teacher
from users.permissions import IsAdminUserRole
from teachers.serializers import TeacherRegisterSerializer, TeacherListSerializer
from classes.serializers import ClassSerializer
from students.models import Student
from students.serializers import StudentSerializer


# Create your views here.
class TeacherRegisterAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserRole]

    def post(self, request):
        serializer = TeacherRegisterSerializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.save()
            return Response({
                "message": "Teacher registered successfully",
                "teacher_id": teacher.id,
                "username": teacher.user.username,
                "email": teacher.user.email,
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teachers = Teacher.objects.select_related('user').all()
        serializer = TeacherListSerializer(teachers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TeacherClassesAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            teacher = Teacher.objects.get(id=id)
        except Teacher.DoesNotExist:
            return Response({"detail": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)

        classes = teacher.classes.all()
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TeacherStudentsAPIView(APIView):
    permission_classes = [IsAuthenticated]  # or AllowAny

    def get(self, request, id):
        try:
            teacher = Teacher.objects.get(id=id)
        except Teacher.DoesNotExist:
            return Response({"detail": "Teacher not found."}, status=status.HTTP_404_NOT_FOUND)

        students = Student.objects.filter(classes__teacher=teacher).distinct()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
