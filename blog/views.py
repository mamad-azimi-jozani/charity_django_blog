from django.shortcuts import render
from .models import Post
# Create your views here.
def index_view(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'blog/blog.html', context)

def detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {
        "post" : post
    }
    return render(request, 'blog/detail.html', context)
