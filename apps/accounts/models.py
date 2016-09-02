from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    GENDER = (
        ('m','Male'),
        ('f','Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER, default='f')
    user = models.ForeignKey(User)
