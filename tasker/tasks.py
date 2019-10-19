from celery import shared_task

@shared_task
def action_client(action="Call", client="Akshay"):
    return (action+" "+client)