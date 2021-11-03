from django.contrib.auth.models import User

from rest_framework import generics

from .models import StudentGroup, Student, Lecture, LessonRoom, Lesson, Timetable

from .serializers import (StudentGroupListSerializer, StudentListSerializer,
                          StudentGroupDetailSerializer, StudentDetailSerializer,
                          UserSerializer, LectureSerializer, LessonRoomSerializer,
                          LessonListSerializer, LessonDetailSerializer, TimetableSerializer)

from .services import get_timetable_today_for_groups, write_json_file


class UserList(generics.ListAPIView):
    """Displaying all users"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """Displaying user detail"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class StudentGroupListView(generics.ListCreateAPIView):
    """Displaying all student groups, creation of a student group"""
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupListSerializer

    # Write today timetable to the json file
    groups = StudentGroup.objects.all().values('number')
    data = get_timetable_today_for_groups(groups)
    write_json_file(data, 'timetable.json')


class StudentGroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Displaying the full student group description, updating and deletion of a group"""
    queryset = StudentGroup.objects.all()
    serializer_class = StudentGroupDetailSerializer


class StudentListView(generics.ListAPIView):
    """Displaying all students"""
    queryset = Student.objects.all()
    serializer_class = StudentListSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Displaying the full information about a student , updating and deletion of a student"""
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer


class StudentCreateView(generics.CreateAPIView):
    """Creation of a student"""
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer


class LectureListView(generics.ListCreateAPIView):
    """Displaying all lectures, creation of a lecture"""
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class LectureDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Displaying the full information about a lecture, updating and deletion of a lecture"""
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer


class LessonRoomListView(generics.ListCreateAPIView):
    """Displaying all lesson rooms, creation of a room"""
    queryset = LessonRoom.objects.all()
    serializer_class = LessonRoomSerializer


class LessonRoomDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Displaying the full information about a lesson room, updating and deletion of a room"""
    queryset = LessonRoom.objects.all()
    serializer_class = LessonRoomSerializer


class LessonListView(generics.ListAPIView):
    """Displaying all lessons, creation of a lesson"""
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer


class LessonDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Displaying the full information about a lesson, updating and deletion of a lesson"""
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer


class LessonCreateView(generics.CreateAPIView):
    """Creation of a lesson"""
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer


class TimetableView(generics.ListAPIView):
    """Represent a Timetable"""
    pass
