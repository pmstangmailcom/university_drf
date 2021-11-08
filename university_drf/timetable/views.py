from datetime import datetime

from django.contrib.auth.models import User
from django.core.mail import send_mail

from rest_framework import generics

from .models import StudentGroup, Student, Lecture, LessonRoom, Lesson
from .serializers import (StudentGroupListSerializer, StudentListSerializer,
                          StudentGroupDetailSerializer, StudentDetailSerializer,
                          UserSerializer, LectureSerializer, LessonRoomSerializer,
                          LessonListSerializer, LessonDetailSerializer, TimetableSerializer)

from .services import get_timetable_today_for_groups, write_json_file, get_date_today, send_timetable, get_users_email
from .tasks import send_timetable_today


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


class TimetableView(generics.ListAPIView): # Need to correct,
    """Represent a Timetable for today"""
    #  Endpoint '/api/timetable/' does not work correctly.
    #  TimetableView (or LessonForTimetableSerializer) need to correct.
    #  It don't show groups not having lesson today (it's right), but timetable for groups having lesson today
    #  include not today's lessons for these groups
    #  Function 'get_timetable_today_for_groups' for json file is correct.
    date = get_date_today()
    queryset = StudentGroup.objects.all().filter(lesson_for_group__lesson_date=date).distinct('number')
    serializer_class = TimetableSerializer

    # Write today timetable to the json file
    groups = queryset.values('number')
    data = get_timetable_today_for_groups(groups)
    write_json_file(data, 'timetable.json')

