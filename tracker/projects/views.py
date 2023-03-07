from django.shortcuts import render
from projects.models import Project


# Create your views here.
def project_list(request, id=id):
    projects = Project.objects.all()
    context = {
        "projects": projects,
    }
    return render(request, "projects/list.html", context)
