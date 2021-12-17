from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(error_messages={
        'required': 'Please enter your name'
    })
    email = forms.EmailField(error_messages={
        'required': 'Please enter your email'
    })
    subject = forms.CharField(error_messages={
        'required': 'Please enter subject'
    })
    message = forms.CharField(widget=forms.Textarea, error_messages={
        'required': 'please enter message'
    })
    class Meta:
        model = Contact
        fields = "__all__"
