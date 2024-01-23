from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings

"""
celery -A core.celery worker --pool=solo -l info [for celery worker]

celery -A core.celery worker --detach  --pool=solo -l info [in daemon mode]

"""
# celery main config

os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')

app=Celery('core')
app.conf.enable_utc=False
app.conf.update(timezone='Asia/Kolkata')

app.config_from_object(settings,namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_tsak(self):
    try:
        print(f'request : {self.request!r}')
    except Exception as e:
        print(str(e))