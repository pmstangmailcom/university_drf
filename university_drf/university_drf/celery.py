import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'university_drf.settings')

app = Celery('university_drf')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
