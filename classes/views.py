from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import ClassSerializer
from users.permissions import IsAdminUserRole

class ClassCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserRole]

    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            class_instance = serializer.save()
            return Response(ClassSerializer(class_instance).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
