from django.urls import path
from .views import *

app_name = "portfolio"

urlpatterns = [
    path("",portfolio_home,name='phome'),
    path("about",about,name= 'about'),
    path("projects",projects,name= 'projects'),
    path('skills',skills,name="skills"),
    path('templates/<int:temp_id>/', front_projects, name='front_projects'),
    path('templates/<int:temp_id>/<str:page>', front_projects, name='front_projects')
]