from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Post, Comment
import requests


# def hello_world(request):
#     return HttpResponse('<input type="button" value="Нажать" data-color="red" >')

class PostListView(ListView):
    queryset = Post.objects.draft()
    template_name = 'article/index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'article/post_detail.html'
