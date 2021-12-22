from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index_view(request, **kwargs):
    posts = Post.objects.filter(status=1)

    if kwargs.get("cat_name"):
        posts = posts.filter(category__name=kwargs.get("cat_name"))
    if kwargs.get("author_name"):
        posts = posts.filter(author__username=kwargs.get("author_name"))
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 2)

    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except EmptyPage:
        posts = posts.page(1)
    except PageNotAnInteger:
        posts = posts.page(1)

    context = {"posts": posts}
    return render(request, 'blog/blog.html', context)

def detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=1)
    context = {
        "post" : post
    }
    return render(request, 'blog/detail.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(title__contains=request.GET.get('s'))
    context = {"posts": posts}
    return render(request, 'blog/blog.html', context)

