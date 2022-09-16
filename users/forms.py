from dataclasses import field
from django import forms
from users.models import CustomUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
