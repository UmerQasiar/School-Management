from rest_framework import serializers
from classes.models import Class
from django.contrib.auth.models import User
from users.models import Profile
from students.models import Student


class StudentRegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField(required=False)
    password = serializers.CharField(write_only=True)
    enrollment_number = serializers.CharField(required=False)
    classes = serializers.ListField(
        child=serializers.IntegerField(), required=True
    )

    def validate_classes(self, class_ids):
        if not class_ids or len(class_ids) == 0:
            raise serializers.ValidationError("At least one class id is required.")

        existing_ids = Class.objects.filter(id__in=class_ids).values_list('id', flat=True)
        invalid_ids = set(class_ids) - set(existing_ids)

        if invalid_ids:
            raise serializers.ValidationError(f"Invalid class IDs: {list(invalid_ids)}")

        return class_ids

    def create(self, validated_data):
        username = validated_data['username']
        email = validated_data.get('email', '')
        password = validated_data['password']
        enrollment_number = validated_data.get('enrollment_number', '')
        class_ids = validated_data.get('classes', [])

        user = User.objects.create_user(username=username, email=email, password=password)
        Profile.objects.create(user=user, role='student')
        student = Student.objects.create(user=user, enrollment_number=enrollment_number)

        if class_ids:
            student.classes.set(Class.objects.filter(id__in=class_ids))

        return student

class StudentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    classes = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'username', 'email', 'enrollment_number', 'classes']

    def get_classes(self, student):
        return [cls.section for cls in student.classes.all()]
