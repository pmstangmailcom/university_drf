from django.contrib.auth.models import User
from django.db import models


class StudentGroup(models.Model):
    """Student group"""
    number = models.CharField(max_length=20, verbose_name='number')  # the number can include string characters

    def __str__(self):
        return self.number


class Student(models.Model):
    """Student"""
    name = models.CharField(max_length=150, verbose_name='name')
    student = models.OneToOneField(User, related_name='student', verbose_name='student', on_delete=models.RESTRICT)
    group = models.ForeignKey(StudentGroup, related_name='students_in_group', verbose_name='student_group',
                              on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class Lecture(models.Model):
    """Lecture"""
    title = models.CharField(max_length=150, verbose_name='title')

    def __str__(self):
        return self.title


class LessonRoom(models.Model):
    """Room for the lesson"""
    number = models.CharField(max_length=10,
                              verbose_name='number')  # the number can include string characters like 101a

    def __str__(self):
        return self.number


class Lesson(models.Model):
    """Lesson"""
    lecture = models.ForeignKey(Lecture, related_name='lecture_to_lesson', verbose_name='lecture',
                                on_delete=models.RESTRICT)
    student_group = models.ForeignKey(StudentGroup, related_name='lesson_for_group', verbose_name='group',
                                      on_delete=models.RESTRICT, null=True)
    lecture_room = models.ForeignKey(LessonRoom, related_name='room_for_lesson', verbose_name='room',
                                     on_delete=models.RESTRICT)
    lesson_date = models.DateField()

    def __str__(self):
        return f'{self.lesson_date} - {self.lecture}'


class Timetable(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='lessons', verbose_name='lesson', on_delete=models.RESTRICT)
    group = models.ForeignKey(StudentGroup, related_name='timetable_for_group', verbose_name='group',
                              on_delete=models.RESTRICT)
    timetable_date = models.DateField()

    def __str__(self):
        return f'Timetable for {self.group} - {self.timetable_date}'
