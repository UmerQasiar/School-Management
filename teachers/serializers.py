from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import Profile
from .models import Teacher


class TeacherRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)
    employee_id = serializers.CharField(required=False)
    date_joined = serializers.DateField(required=False)

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']

        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, role='teacher')
        teacher = Teacher.objects.create(
            user=user,
            employee_id=validated_data.get('employee_id', ''),
            date_joined=validated_data.get('date_joined')
        )

        return teacher
