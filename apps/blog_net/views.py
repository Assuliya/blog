from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import Entry
from forms import ContactForm
from django.core.mail import send_mail, mail_admins


def index(request):
    entries = Entry.objects.published_entries().order_by('-id')
    ctx = { 'entries': entries}
    return render(request, 'blog_net/index.html', ctx)

def about(request):

    # ctx = { 'entries': entries}
    return render(request, 'blog_net/about.html')

def archive(request):

    # ctx = { 'entries': entries}
    return render(request, 'blog_net/archive.html')

def contact(request):

    success = False
    email = ''
    title = ''
    text = ''

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            success = True
            email = contact_form.cleaned_data['email']
            title = contact_form.cleaned_data['title']
            text = contact_form.cleaned_data['text']


            # send_mail("Message from Blog","title: %s \ntext: %s \nemail: %s" %(title,text,email), "sends from my email to mine", [settings.EMAIL_HOST_USER])

    else:
        contact_form = ContactForm()

    ctx = { 'contact_form': contact_form, 'email': email, 'title': title, 'text': text, 'success': success}
    return render(request, 'blog_net/contact.html', ctx)
