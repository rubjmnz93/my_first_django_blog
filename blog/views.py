from django.shortcuts import render
from django.utils import timezone
from django.views import generic

from .models import Post


class PostListView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-published_date')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'