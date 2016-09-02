from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User
from models import UserProfile

@login_required
def profile(request):
    user = UserProfile.objects.get(id=request.user.id)
    ctx = {
        'profile':user
    }
    return render(request, 'accounts/profile.html', ctx)
