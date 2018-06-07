from django.shortcuts import render
from .models import Post, Comment

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'scribble/post_detail.html', {'post': post})

def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'scribble/comment_list.html',{'comments': comments})

def comment_detail(request, pk):
    post = Comment.objects.get(id=pk)
    return render(request, 'scribble/comment_detail.html', {'comment': comment})