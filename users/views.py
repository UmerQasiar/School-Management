from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from .permissions import IsAdminUserRole
from django.contrib.auth.models import User

class CurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

class UserListAPIView(APIView):
    permission_classes = [IsAuthenticated, IsAdminUserRole]

    def get(self, request):
        users = User.objects.select_related('profile').all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)