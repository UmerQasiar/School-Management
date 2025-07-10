from rest_framework import serializers
from .models import Class
from teachers.models import Teacher


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = ['id', 'section', 'teacher']

    def validate_teacher(self, value):
        if not Teacher.objects.filter(id=value.id).exists():
            raise serializers.ValidationError("Teacher not found.")
        return value
