from django import template
from ..models import Post, Category
from django.shortcuts import render
register = template.Library()

@register.simple_tag(name='recent_posts')
def sample():
    posts = Post.objects.filter(status=1)[:5]
    return posts

@register.simple_tag(name='post_category')
def sample():
    posts = Post.objects.filter(status=1)
    cat = Category.objects.all()
    cat_dict = {}
    for i in cat:
        cat_dict[i] = posts.filter(category=i).count()
    return cat_dict