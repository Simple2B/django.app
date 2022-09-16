from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserCreateForm


class RegisterUserView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/register_user.html'
    success_url = reverse_lazy('register_user')
