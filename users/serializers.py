from rest_framework import serializers
from django.contrib.auth.models import User

class CurrentUserSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source='profile.role')

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
