from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.create_task, name="create_task"),
    path('all/', views.list_tasks, name='list_tasks'),
    path('timespan/', views.list_tasks_within_timespan, name='list_tasks_within_timespan'),
    path('get/<int:task_id>/', views.get_task, name='get_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('get/dog/<int:dog_id>/', views.list_tasks_for_dog, name='list_tasks_for_dog'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('patch/<int:task_id>/', views.partial_update_task, name='partial_update_task'),

]
