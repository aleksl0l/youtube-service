import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "umniy_polis_test.settings")

app = Celery("umniy_polis_test", include=["core.tasks"])
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
