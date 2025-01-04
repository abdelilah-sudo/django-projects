from django.urls import path
from .views import *
app_name = "fullstack"
create_superuser()  # Automatically create superuser during deployment

urlpatterns = [
    path('',home,name= "home"),
    path('topics/',topics,name='topics'),
    path("topics/<int:topic_id>/",topic,name="topic"),
    path('new_topic/', new_topic, name='new_topic'),
    path("new_entry/<int:topic_id>",new_entry,name="new_entry"),
    path("delete_topic/<int:topic_id>",delete_topic,name="delete_topic"),
    path('edit_entry/<int:entry_id>/', edit_entry, name='edit_entry'),
    path("delete_entry/<int:entry_id>",delete_entry,name="delete_entry"),

]