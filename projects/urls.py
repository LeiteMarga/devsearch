from django.urls import path
from .           import views


urlpatterns = [
    path('',                    views.projects,         name="projects"),
    path('project/<pk>',        views.project,          name="project"),
    path('create_project/',     views.createProject,    name="create_project"),
    path('update_project/<pk>', views.updateProject,    name="update_project"),
    path('delete_project/<pk>', views.deleteProject,    name="delete_project"),
]