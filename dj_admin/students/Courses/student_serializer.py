from rest_framework import serializers
from .models import Courses
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class CourseSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=True)  # Correctly map the ForeignKey field

    class Meta:
        model = Courses
        fields = ['id', 'student', 'course', 'is_active', 'created_at', 'updated_at']  # Include all required fields
