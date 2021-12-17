from django.shortcuts import render
from .forms import ContactForm
from .models import Contact
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def index_view(request):
    return render(request, 'home/index.html')

def about_view(request):
    return render(request, 'home/about.html')

def contact_view(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact request submitted successfully')
            return render(request, 'home/contact.html', {'form': ContactForm(request.GET)})
        else:
            messages.error(request, 'Invalid form submission.')
            messages.error(request, form.errors)

    context = {
        "form": form
    }
    return render(request, 'home/contact.html', context)