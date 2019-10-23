from django.urls import path

from . import views

app_name = 'tasker'
urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:task_id>/', views.TaskView, name='TaskView'),
    path('tasks/', views.AllTasksView, name='AlltasksView'),
    #path('task/<int:task_id>/', views.TaskView.as_view(), name='task'),
    #path('tasks/', views.AllTasksView.as_view(), name='alltasks'),
]