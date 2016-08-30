from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
# from models import User, Book, Review


def index(request):
    return render(request, 'blog_net/index.html')
