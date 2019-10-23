import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmaster.settings')

celery_app = Celery('taskmaster')
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks('CELERY')

@celery_app.task
def test(arg):
    print(arg)

celery_app.conf.beat_schedule = {
    'complete-every-30-seconds': {
        'task': 'tasks.add',
        'schedule': 30.0,
    },
}
celery_app.conf.timezone = 'UTC'
