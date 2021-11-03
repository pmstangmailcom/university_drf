from django.contrib.auth.models import User
from rest_framework import serializers

from .models import StudentGroup, Student, Lecture, LessonRoom, Lesson, Timetable


class UserSerializer(serializers.ModelSerializer):
    """Serializer for all users"""

    class Meta:
        model = User
        fields = ['username', 'email']


class StudentListSerializer(serializers.ModelSerializer):
    """Serializer for all students"""
    group = serializers.SlugRelatedField(slug_field='number', read_only=True)  # show group number, not id
    email = serializers.SlugRelatedField(slug_field='email', queryset=User.objects.all(), source='student')

    class Meta:
        model = Student
        fields = ('name', 'group', 'id', 'email')
        read_only_fields = ('id',)


class StudentDetailSerializer(serializers.ModelSerializer):
    """Serializer for the full information about a student"""
    group = serializers.SlugRelatedField(slug_field='number', queryset=StudentGroup.objects.all())
    student = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Student
        fields = ('name', 'group', 'student')


class StudentGroupListSerializer(serializers.ModelSerializer):
    """Serializer for all student groups"""

    class Meta:
        model = StudentGroup
        fields = ('number',)


class StudentGroupDetailSerializer(serializers.ModelSerializer):
    """Serializer for the full student group description"""
    students_in_group = StudentListSerializer(many=True, read_only=True)

    class Meta:
        model = StudentGroup
        fields = ('number', 'students_in_group')


class LectureSerializer(serializers.ModelSerializer):
    """Serializer for a lecture"""

    class Meta:
        model = Lecture
        fields = ('title',)


class LessonRoomSerializer(serializers.ModelSerializer):
    """Serializer for a lesson room"""

    class Meta:
        model = LessonRoom
        fields = ('number',)


class LessonListSerializer(serializers.ModelSerializer):
    """Serializer for all lessons"""
    lecture = LectureSerializer()

    class Meta:
        model = Lesson
        fields = ('lecture', 'lesson_date', 'id')
        read_only_fields = ('id',)


class LessonDetailSerializer(serializers.ModelSerializer):
    """Serializer for the full information about a lesson"""
    lecture = serializers.SlugRelatedField(slug_field='title', queryset=Lecture.objects.all())
    lecture_room = serializers.SlugRelatedField(slug_field='number', queryset=LessonRoom.objects.all())
    student_group = serializers.SlugRelatedField(slug_field='number', queryset=StudentGroup.objects.all())
    lesson_date = serializers.DateField()

    class Meta:
        model = Lesson
        fields = ('lecture', 'student_group', 'lecture_room', 'lesson_date', 'id')
        read_only_fields = ('id',)

class TimetableSerializer(serializers.ModelSerializer):
    """Serializer for timetable"""
    pass


