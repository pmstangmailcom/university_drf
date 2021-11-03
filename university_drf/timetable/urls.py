from django.urls import path

from .views import (StudentGroupListView, StudentGroupDetailView,
                    StudentListView, StudentDetailView, StudentCreateView, UserList, UserDetail,
                    LectureListView, LectureDetailView, LessonRoomListView, LessonRoomDetailView,
                    LessonListView, LessonDetailView, LessonCreateView, TimetableView)

app_name = 'timetable'

urlpatterns = [

    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),

    path('groups/', StudentGroupListView.as_view()),
    path('groups/<int:pk>/', StudentGroupDetailView.as_view()),

    path('students/', StudentListView.as_view()),
    path('students/<int:pk>/', StudentDetailView.as_view()),
    path('student/', StudentCreateView.as_view()),

    path('lectures/', LectureListView.as_view()),
    path('lectures/<int:pk>/', LectureDetailView.as_view()),

    path('rooms/', LessonRoomListView.as_view()),
    path('rooms/<int:pk>/', LessonRoomDetailView.as_view()),

    path('lessons/', LessonListView.as_view()),
    path('lessons/<int:pk>/', LessonDetailView.as_view()),
    path('lesson/', LessonCreateView.as_view()),

    path('timetable/', TimetableView.as_view()),

]
