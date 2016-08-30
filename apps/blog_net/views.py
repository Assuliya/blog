from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import Entry


def index(request):
    entries = Entry.objects.published_entries().order_by('-id')
    ctx = { 'entries': entries}
    return render(request, 'blog_net/index.html', ctx)
