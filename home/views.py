from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    return render(request, 'home/index.html')

def about_view(request):
    return render(request, 'home/about.html')

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    context = {
        "form": form
    }
    return render(request, 'home/contact.html', context)