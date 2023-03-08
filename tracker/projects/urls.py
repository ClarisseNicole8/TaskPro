from django.urls import path


from projects.views import (
    list_projects,
    show_project,
)


urlpatterns = [
    path("", list_projects, name="home"),
    path("<int:id>/", show_project, name="show_project"),
]
