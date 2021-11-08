from datetime import datetime
import json

from django.conf import settings
from django.core.mail import send_mail

from .models import Lesson, Student


def get_date_today():
    """Get date today"""
    date = datetime.today()
    return date


def get_timetable_today_for_groups(groups: list) -> list:
    """Get list of today lessons for each group, output list of dicts, group number: list of lessons"""
    date = datetime.today()
    timetable_for_groups = []
    for group in groups:
        lessons = list(Lesson.objects.filter(lesson_date=date).filter(student_group__number=group['number']).values(
            'lecture__title', 'lecture_room__number', ))
        if lessons:
            timetable_for_groups.append({group['number']: lessons})
    return timetable_for_groups


def write_json_file(data, filename):
    """Write data to json file"""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=1)


def write_file(data, filename):
    """Write data to file"""
    with open(filename, 'w') as f:
        f.write(data)


def get_users_email(group_number: str) -> list:
    """Get list of users' email in a group"""
    emails_list = list(Student.objects.all().filter(group__number=group_number).values_list('student__email'))
    emails_list = [item[0] for item in emails_list if item[0]]
    return emails_list


def send_timetable(groups: list) -> None:
    """Send timetable to students having lessons today"""
    #  It need to write a new function instead of 'get_timetable_today_for_groups' to get str data to send it by email
    subject = 'Your timetable for today'
    for group in groups:
        email_list = get_users_email(group['number'])
        data = str(get_timetable_today_for_groups([group]))
        send_mail(subject, data, settings.EMAIL_HOST_USER, email_list)
