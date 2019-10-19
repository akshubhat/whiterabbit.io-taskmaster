# whiterabbit.io-taskmaster


## Introduction

This is an example of asynchronus microservice using django and celery. Redis is used as task broker. Celery worker-node acts as a consumer of the task broker and runs the tasks. Therefore no callback scenario is available in this approach.

###To install:
	
	pip3 install requirements.txt
	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver

###To create admin:
	
	python3 manage.py createsuperuser

###To run the celeryd using django manage.py

	$ python manage.py celeryd -l info
	
###Curl to the endpoint

	$ curl -i http://localhost:8000/ping/
	
###To see the list of tasks in Redis
	
	$ redis-server &

	$ redis-cli
	$ 127.0.0.1:6379> keys *

###Testing

Run these commands in different terminals:
	
	$ redis-server &
	$ celery worker -A taskmaster --loglevel=info
	$ python3 manage.py shell

In python shell, create and test the task:

	>>> from tasker.tasks import action_client
	>>> task = action_client.dealay("Message", "Ambi")
	>>> task = action_client.delay("Message", "Ambi")
	>>> print(f"id={task.id}, state={task.state}, status={task.status}")
	>>> task.get()

###References:

	https://stackabuse.com/asynchronous-tasks-in-django-with-redis-and-celery/
	https://docs.djangoproject.com/en/2.2/intro/tutorial01/