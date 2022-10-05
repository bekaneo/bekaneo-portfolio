from django.shortcuts import render
from django.views import generic
from blog.models import Post, Comment
from blog.forms import CommentForm


class BlogIndexView(generic.ListView):
    model = Post
    context_object_name = 'posts'


class BlogDetailView(generic.DetailView, generic.FormView):
    @staticmethod
    def get(request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        comments = Comment.objects.filter(post=post)
        form = CommentForm(request.POST)
        context = {
            'post': post,
            'comments': comments,
            'form': form
        }
        return render(request, 'blog_detail.html', context)

    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
        return BlogDetailView.get(request, pk)


class CategoryView(generic.ListView):
    def get(self, request, category, *args, **kwargs):
        posts = Post.objects.filter(categories__name__contains=category).order_by('-created_on')
        context = {
            "category": category,
            "posts": posts
        }
        return render(request, "blog_category.html", context)
