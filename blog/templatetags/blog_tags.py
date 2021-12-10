from django import template
from ..models import Post
from django.shortcuts import render
register = template.Library()

@register.simple_tag(name='recent_posts')
def sample():
    posts = Post.objects.filter(status=1)[:5]
    return posts