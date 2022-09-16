from urllib import request
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView

from .forms import UserCreateForm, LoginUserForm


class RegisterUserView(CreateView):
    form_class = UserCreateForm
    template_name = 'users/register_user.html'
    success_url = reverse_lazy('register_user')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUserView(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login_page.html'

    def get_success_url(self) -> str:
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login_user')


def home_page(request):
    from django.shortcuts import render

    return render(request, 'users/index.html')
