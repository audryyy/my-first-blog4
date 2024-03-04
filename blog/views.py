from django.shortcuts import render
from .models import Post #RM

def post_list(request):
    posts = Post.objects.all() #RM
    return render(request, 'blog/post_list.html', {'posts': posts})
