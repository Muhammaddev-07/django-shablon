from celery import shared_task

@shared_task
def my_task (ism):
    print(f"yangi task tushdi", ism)