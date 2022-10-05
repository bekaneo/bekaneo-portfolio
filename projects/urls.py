from django.urls import path
from . import views


urlpatterns = [
    path("", views.ListProjectsView.as_view(template_name='project_index.html'), name="project_index"),
    path("<int:pk>/", views.DetailProjectView.as_view(template_name='project_detail.html'), name="project_detail"),
]
