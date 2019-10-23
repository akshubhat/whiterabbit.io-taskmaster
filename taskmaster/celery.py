import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmaster.settings')

celery_app = Celery('taskmaster')
celery_app.config_from_object('django.conf:settings')
celery_app.autodiscover_tasks('CELERY')