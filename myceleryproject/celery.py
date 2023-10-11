import os

from celery import Celery
from time import sleep
from datetime import timedelta

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myceleryproject.settings")

app = Celery("myceleryproject")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(name="addition_task")
def add(x, y):
    sleep(20)
    return x + y


# Method 2 for scheduling celery tasks
# app.conf.beat_schedule = {
#     "every_10_seconds": {
#         "task": "myapp.tasks.clear_session_cache",
#         "schedule": 10,
#         "args": ("2222",),
#     }
# }

# Using timedelta
# use crontab instead of timedelta for advanced scheduling like calling once a week or calling everyday at certain time
# there is another option called solar to call for sunset sunrise etc
# https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html for more details
app.conf.beat_schedule = {
    "every_10_seconds": {
        "task": "myapp.tasks.clear_session_cache",
        "schedule": timedelta(seconds=10),
        "args": ("3333",),
    }
}
