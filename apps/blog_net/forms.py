from django import forms
from models import Entry

class ContactForm(forms.Form):
    email = forms.EmailField()
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
