from django.conf import settings
from django.core.mail import send_mail
from django.template import Engine, Context

from .models import StudentGroup
from .services import send_timetable
from university_drf.celery import app


@app.task
def send_timetable_today():
    """Once a day send to email timetable to students having lessons this day"""
    groups = StudentGroup.object.all()
    groups_list = list(groups.values('number'))
    send_timetable(groups_list)
    return None
