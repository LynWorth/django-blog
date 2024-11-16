from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    #queryset = Post.objects.all().order_by("created_on")
    #queryset = Post.objects.all().order_by("-created_on")
    #queryset = Post.objects.filter(author=6)
    #queryset = Post.objects.all()
    template_name = "post_list.html"
    