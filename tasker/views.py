from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!! You're at task scheduler app using django, celery and redis.")

def TaskView(request, task_id):
	response = "Task number : %s."
	return HttpResponse(response % task_id)

def AllTasksView(request):
	return HttpResponse("All Tasks.")