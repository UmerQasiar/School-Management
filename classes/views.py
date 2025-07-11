from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ClassSerializer
from users.permissions import IsAdminUserRole
from .models import Class

class ClassCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserRole]

    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            class_instance = serializer.save()
            return Response(ClassSerializer(class_instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClassListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ClassSerializer

    def get_queryset(self):
        user = self.request.user
        role = user.profile.role

        if role == 'admin':
            return Class.objects.all()
        elif role == 'teacher':
            return Class.objects.filter(teacher=user.teacher)
        elif role == 'student':
            return user.student.classes.all()
        return Class.objects.none()
