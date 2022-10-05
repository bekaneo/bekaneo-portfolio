from django.views.generic import ListView, DetailView

from projects.models import Project


class ListProjectsView(ListView):
    model = Project
    context_object_name = 'projects'


class DetailProjectView(DetailView):
    model = Project
    context_object_name = 'project'