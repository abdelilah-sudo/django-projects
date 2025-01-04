from django.urls import path
# Import specific views
from .views import display_tasks,create_tasks,delete_tasks,update_tasks  

# URL patterns for the tasks app
app_name = 'tasks'

urlpatterns = [
    path("", display_tasks, name='display_tasks'),  # Route for displaying tasks
    path("create-task/", create_tasks, name='create_task'),  # Route for creating tasks
    path("delete-all-tasks/", delete_tasks, {'ps': 'All Tasks'}, name='delete_all_tasks'),  # For deleting all tasks
    path("delete-task/<int:pk>", delete_tasks, name='delete_task'),  # Route for creating tasks
    path("update-task/<int:pk>", update_tasks, name='update_task'),  # Route for creating tasks
]
