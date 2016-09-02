from django import forms
from models import UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    gender = forms.ChoiceField(choices=UserProfile.GENDER)
    def save(self, *args, **kwargs):
        user = super(RegisterForm, self).save(*args, **kwargs)
        UserProfile.objects.create(user=user, gender=self.cleaned_data['gender'])
        return user
