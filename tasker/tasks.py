from celery import shared_task
from celery.decorators import task
from .models import ClientTask

@shared_task
def action_client(action="Call", client="Akshay"):
    return (action+" "+client)

@task(name="complete_client_task")
def complete_client_task():
    tasks = ClientTask.objects.all()
    for task in tasks:
        if task.complete_action:
            print("Task completed.")
        else:
            print("Task remaining.")