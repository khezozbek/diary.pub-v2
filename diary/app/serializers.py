from rest_framework import serializers
from .models import CustomUser, Teacher, Group, Student, ExamResult, Parent
from django.contrib.auth import authenticate


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    password = serializers.CharField(write_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user_type = validated_data.get('type')
        if user_type == 'Student':
            level = validated_data.get('level')
            if level and level != 'IELTS':
                student = Student.objects.create(level=level)
                validated_data['student'] = student
        elif user_type == 'Teacher':
            teacher_data = validated_data.pop('teacher', {})
            user = CustomUser.objects.create(**validated_data)
            teacher = Teacher.objects.create(user=user, **teacher_data)
            validated_data['teacher'] = teacher

        return validated_data


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        fields = '__all__'


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'
