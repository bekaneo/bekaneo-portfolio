from django.urls import path
from . import views

urlpatterns = [
    path("", views.BlogIndexView.as_view(template_name='blog_index.html'), name="blog_index"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("<category>/", views.CategoryView.as_view(), name="blog_category"),
]