from celery import shared_task
from time import sleep


@shared_task
def sub(x, y):
    sleep(30)
    return x - y


@shared_task
def clear_session_cache(id):
    print(f"Session Cache cleared: {id}")
    return id


@shared_task
def clear_redis_data(id):
    print(f"Redis data cleared: {id}")
    return id
