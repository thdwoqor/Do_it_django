from django.shortcuts import render
from django.urls.resolvers import URLPattern
from .models import Post
# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',{
            'posts':posts,
        }
    )