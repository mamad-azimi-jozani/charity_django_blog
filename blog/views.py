from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'blog/blog.html')

def detail_view(request):
    return render(request, 'blog/detail.html')
