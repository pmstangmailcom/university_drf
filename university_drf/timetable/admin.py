from django.contrib import admin

from .models import StudentGroup, Student, Lecture, LessonRoom, Lesson

admin.site.register(StudentGroup)
admin.site.register(Student)
admin.site.register(Lecture)
admin.site.register(LessonRoom)
admin.site.register(Lesson)
