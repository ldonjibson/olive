import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'olive_app.settings.productions')

app = Celery('olive_app')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_heartbeat=0
app.autodiscover_tasks()

# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saas_vbp.settings')

# from django.conf import settings

# from tenant_schemas_celery.app import CeleryApp

# app = CeleryApp()
# app.config_from_object('django.conf:settings')
# app.conf.broker_heartbeat=0
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)