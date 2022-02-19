from django.shortcuts import render
from django.views import View
from django.views import generic
from blog.models import Post, Topic


# Create your views here.


class PostListView(generic.ListView):
    model = Post


class PostDetailView(generic.DetailView):
    model = Post


class TopicListView(generic.ListView):
    model = Topic


class TopicDetailView(generic.DetailView):
    model = Topic


def contact(request):
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, "blog/about.html")
