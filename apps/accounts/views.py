from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from models import UserProfile
from forms import RegisterForm



@login_required
def profile(request):
    user = UserProfile.objects.get(user__id=request.user.id)
    ctx = {
        'profile':user
    }
    return render(request, 'accounts/profile.html', ctx)

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.backend = settings.AUTHENTICATION_BACKENDS[0]

            login(request, user)
            return redirect(reverse('accounts_profile'))

    ctx = {
        'form': form
    }

    return render(request, 'accounts/register.html', ctx)
