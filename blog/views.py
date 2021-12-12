from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.
def index_view(request, cat_name=None):
    posts = Post.objects.filter(status=1)
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    context = {"posts": posts}
    return render(request, 'blog/blog.html', context)

def detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=1)
    context = {
        "post" : post
    }
    return render(request, 'blog/detail.html', context)

def author_view(request, author_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(author__username=author_name)
    context = {"posts": posts}
    return render(request, 'blog/blog.html', context)

