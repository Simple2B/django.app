from dataclasses import field
from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
