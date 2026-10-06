from django.shortcuts import render
from .models import BlogPost


def home(request):
    posts = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
