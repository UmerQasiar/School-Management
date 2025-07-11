from rest_framework import serializers
from .models import Subject

class SubjectSerializer(serializers.ModelSerializer):
    class_section = serializers.CharField(source='class_assigned.section', read_only=True)

    class Meta:
        model = Subject
        fields = ['id', 'name', 'class_assigned', 'class_section']
